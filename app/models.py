from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required

from app import app

# Database
# Create database connection object
db = SQLAlchemy(app)

# Constants
SEX_TYPES = [
    'Male',
    'Female',
    'Other',
]

# Define models
roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model, UserMixin):
    id =  db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200))
    sex = db.Column('sex', db.Integer, nullable=False, default=1)

    def __init__(self, description, sex):
        self.description = description
        self.sex = sex

    def _get_sex(self):
        return SEX_TYPES[self.sex]

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

# Create an admin user
import os
if os.access(os.path.join('app.db'), os.R_OK) is False:
    db.create_all()
    # Create an admin user
    user_datastore.create_user(email=app.config['ADMIN_EMAIL'], password=app.config['ADMIN_PW'])
    db.session.commit()

    # Create seed data
    for n in range(1, 10):
        c = Content('Description {}'.format(n), 'male')
        db.session.add(c)
        db.session.commit()
