"""
Copyright 2016 Brian Quach
Licensed under MIT (https://github.com/brianquach/udacity-nano-fullstack-catalog/blob/master/LICENSE)  # noqa
"""
import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from oauth2client.file import Storage


# Used to store and retrieve google's credential object for api calls
G_CREDENTIAL_STORAGE = Storage('credential_storage')

# This app's client Id to generate an access token from Google's OAuth API
CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read()
)['web']['client_id']

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///catalog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from catalog import views  # noqa
