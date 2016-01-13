from catalog import app, db, CLIENT_ID
from catalog.models import User, Catagory, CatagoryItem
from flask import (
    Flask,
    url_for,
    render_template,
    redirect,
    request,
    flash,
    jsonify,
    session,
    make_response
)
from oauth2client import client
from apiclient import discovery, errors as gErrors
import random, string, httplib2, json


@app.route('/')
@app.route('/dashboard')
def dashboard():
    return render_template(
        'index.html'
    )

@app.route('/login')
def login():
    # Create anti-forgery state token
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
    authorization_token = request.data
    state_token = request.args.get('state')

    # Ensure anti-forgery state token is from the expected user making
    # this call
    if state_token != session.get('state'):
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
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
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'),
            401
        )
        response.headers['Content-Type'] = 'application/json'
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
        response = make_response(
            json.dumps(error.get('error_description')),
            400
        )
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if token_info['user_id'] != gplus_id:
        response = make_response(
            json.dumps('Token\'s user ID doesn\'t match given user ID.'),
            401
        )
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if token_info['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps('Token\'s client ID does not match app\'s.'), 401)
        response.headers['Content-Type'] = 'application/json'
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
    user_id = getUserID(email)
    if user_id is None:
        user_id = createUser(session)
    session['user_id'] = user_id
    
    flash('you are now logged in as {0}'.format(username))
    response = make_response(
        json.dumps(userinfo),
        200
    )
    response.headers['Content-Type'] = 'application/json'
    return response

# User Helper Functions
def createUser(session):
    newUser = User(
        name=session['username'],
        email=session['email'],
        picture=session['picture']
    )
    db.session.add(newUser)
    db.session.commit()
    user = User.query.filter_by(email=session['email']).one()
    return user.id


def getUserInfo(user_id):
    user = User.query.filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = User.query.filter_by(email=email).one()
        return user.id
    except:
        return None
