import os
from flask import Flask
from flask_security import Security

from .views import app
from . import models

# Connect sqlalchemy to app
models.db.init_app(app)

# Setup Flask-Security
security = Security(app, models.user_datastore)

@app.cli.command()
def initdb():
    models.init_db(app.config['ADMIN_EMAIL'], app.config['ADMIN_PW'])
