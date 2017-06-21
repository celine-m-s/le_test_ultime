import os
from flask import Flask
from flask_security import Security

from .views import fbapp
from . import models

# Connect sqlalchemy to app
models.db.init_app(fbapp)

# Setup Flask-Security
security = Security(fbapp, models.user_datastore)

@fbapp.cli.command()
def initdb():
    models.init_db(fbapp.config['ADMIN_EMAIL'], fbapp.config['ADMIN_PW'])
