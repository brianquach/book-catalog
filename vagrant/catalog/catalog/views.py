"""
Copyright 2016 Brian Quach
Licensed under MIT (https://github.com/brianquach/udacity-nano-fullstack-catalog/blob/master/LICENSE)  # noqa
"""
import httplib2
import json
import random
import string
from apiclient import discovery
from apiclient import errors as gErrors
from dicttoxml import dicttoxml
from flask import flash
from flask import Flask
from flask import jsonify
from flask import make_response
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from oauth2client import client
from catalog import app
from catalog import CLIENT_ID
from catalog import db
from catalog.models import Catagory
from catalog.models import CatagoryItem
from catalog.models import User


@app.route('/')
@app.route('/dashboard')
def dashboard():
    """Construct main page.

    Returns:
        A HTML page representing the index page.
    """
    return render_template(
        'index.html'
    )


@app.route('/login')
def login():
    """Construct login page.

    Creates and adds an anti-forgery state token to the session for oauth login
    authentication.

    Returns:
        A HTML page representing the login page.
    """
    state = ''.join(
        random.choice(
            string.ascii_uppercase + string.digits
        ) for x in xrange(32)
    )
    session['state'] = state
    return render_template(
        'login.html',
        client_id=CLIENT_ID,
        state=state
    )


@app.route('/server-connect', methods=['POST'])
def server_oauth():
    """Authenticate a user using OAuth through Google's API.

    Verifies that the user is the one actually making the call and that the
    access token return is intended for this application.

    Returns:
      A userinfo object:
        family_name: "A String", The user's last name.
        name: String, The user's full name.
        picture: String, URL of the user's picture image.
        locale: String, The user's preferred locale.
        gender: String, The user's gender.
        id: String, The obfuscated ID of the user.
        link: String, URL of the profile page.
        given_name: String, The user's first name.
        email: String, The user's email address.
        hd: String, The hosted domain e.g. example.com if the user is Google
          apps user.
        verified_email: Boolean, true if the email address is verified. Always
          verified because we only return the user's primary email address.
    """
    authorization_token = request.data
    state_token = request.args.get('state')

    # Ensure anti-forgery state token is from the expected user making
    # this call
    if state_token != session.get('state'):
        response = jsonify(json.dumps('Invalid state parameter.'), 401)
        response.status_code = 401
        return response

    try:
        # Create flow object to help aquire user credentials
        flow = client.flow_from_clientsecrets(
            'client_secrets.json',
            scope='',
            redirect_uri='postmessage'
        )

        # Exchange authorization token for access code
        credentials = flow.step2_exchange(authorization_token)
    except client.FlowExchangeError:
        response = jsonify('Failed to upgrade the authorization code.')
        response.status_code = 401
        return response

    # Apply acess token to http object
    http_auth = credentials.authorize(httplib2.Http())

    access_token = credentials.access_token
    # Build service call to google for user profile information
    oauth_service = discovery.build('oauth2', 'v2', http_auth)
    http_request = oauth_service.tokeninfo(access_token=access_token)
    try:
        token_info = http_request.execute()
    except gErrors.HttpError, err:
        error = json.loads(err.content)
        response = jsonify(error.get('error_description'))
        response.status_code = 400
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if token_info['user_id'] != gplus_id:
        response = jsonify('Token\'s user ID doesn\'t match given user ID.')
        response.status_code = 401
        return response

    # Verify that the access token is valid for this app.
    if token_info['issued_to'] != CLIENT_ID:
        response = jsonify('Token\'s client ID does not match app\'s.')
        response.status_code = 401
        return response

    # stored_credentials = session.get('credentials')
    # stored_gplus_id = session.get('gplus_id')
    # if stored_credentials is not None and gplus_id == stored_gplus_id:
    #     response = make_response(
    #         json.dumps('Current user is already connected.'),
    #         200
    #     )
    #     response.headers['Content-Type'] = 'application/json'
    #     return response

    # Store the access token in the session
    session['credentials'] = credentials.to_json()
    session['gplus_id'] = gplus_id

    userinfo = oauth_service.userinfo().get().execute()

    email = userinfo['email']
    username = userinfo['name']
    session['username'] = username
    session['picture'] = userinfo['picture']
    session['email'] = email

    # create a user account if none associated with email
    user_id = get_user_id(email)
    if user_id is None:
        user_id = create_user(session)
    session['user_id'] = user_id

    flash('you are now logged in as {0}'.format(username))
    return jsonify(userinfo)


# User Helper Functions
def create_user(session):
    """Add a new user into the database.

    Args:
      session: object containing user's information from oauth provider.

    Returns:
      Newly added user object.
    """
    newUser = User(
        name=session['username'],
        email=session['email'],
        picture=session['picture']
    )
    db.session.add(newUser)
    db.session.commit()
    user = User.query.filter_by(email=session['email']).one()
    return user.id


def get_userinfo(user_id):
    """Fetches user information.

    Args:
      user_id: user's id.

    Returns:
      A user object matching given user id.
    """
    user = User.query.filter_by(id=user_id).one()
    return user


def get_user_id(email):
    """Fetches user's id.

    Args:
      email: user's email address.

    Returns:
      User ID of user with given email address.
    """
    try:
        user = User.query.filter_by(email=email).one()
        return user.id
    except:
        return None


# JSON Endpoints
@app.route('/me.json')
def user_json():
    """Fetches JSON representation of logged in user.

    Returns:
      JSON object of currently logged in user, if user is logged in. Otherwise
      an empty JSON object.
    """
    if 'user_id' in session:
        user_id = session['user_id']
        user = User.query.filter_by(id=user_id).one()
        return jsonify(user=user.serialize)
    return jsonify([])


@app.route('/catagory.json')
def catagory_json():
    """Fetches JSON representation of all catagories and their items.

    Returns:
      JSON object of all catagories and their items.
    """
    catagories = Catagory.query.all()
    return jsonify(catagories=[c.serialize for c in catagories])


@app.route('/catagory/<int:catagory_id>/items.json')
def catagory_item_json(catagory_id):
    """Fetches JSON representation of all items in a given catagory.

    Args:
      catagory_id: Id of catagory to fetch items from.

    Returns:
      JSON object of a catagory and its items.
    """
    catagory = Catagory.query.filter_by(id=catagory_id).one()
    catagory_items = CatagoryItem.\
        query.\
        filter_by(catagory_id=catagory_id).\
        all()
    return jsonify(
        catagory=catagory.name,
        catagory_items=[ci.serialize for ci in catagory_items]
    )


@app.route('/me.xml')
def user_xml():
    """Fetches XML representation of logged in user.

    Returns:
      XML file of currently logged in user, if user is logged in. Otherwise
      an empty XML file.
    """
    if 'user_id' in session:
        user_id = session['user_id']
        user = User.query.filter_by(id=user_id).one()
        response = make_response(
            dicttoxml(user.serialize, custom_root='me', attr_type=False),
            200
        )
    else:
        response = make_response(
            '<?xml version="1.0" encoding="UTF-8"?><me></me>',
            401
        )
    response.headers['Content-Type'] = 'text/xml'
    return response


@app.route('/catagory.xml')
def catagory_xml():
    """Fetches XML representation of all catagories and their items.

    Returns:
      XML file of all catagories and their items.
    """
    catagories = Catagory.query.all()
    response = make_response(
        dicttoxml(
            [c.serialize for c in catagories],
            custom_root='catagories',
            attr_type=False
        ),
        200
    )
    response.headers['Content-Type'] = 'text/xml'
    return response


@app.route('/catagory/<int:catagory_id>/items.xml')
def catagory_item_xml(catagory_id):
    """Fetches XML representation of all items in a given catagory.

    Args:
      catagory_id: Id of catagory to fetch items from.

    Returns:
      XML file of a catagory and its items.
    """
    catagory = Catagory.query.filter_by(id=catagory_id).one()
    catagory_items = CatagoryItem.\
        query.\
        filter_by(catagory_id=catagory_id).\
        all()
    response = make_response(
        dicttoxml({
            'name': catagory.name,
            'items': [ci.serialize for ci in catagory_items]
        }, custom_root='catagory', attr_type=False),
        200
    )
    response.headers['Content-Type'] = 'text/xml'
    return response
