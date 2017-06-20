from flask_sqlalchemy import SQLAlchemy
from flask_security import SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin

# Database
# Create database connection object
db = SQLAlchemy()

# Define models
roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
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

    GENDER_FEMALE = 0
    GENDER_MALE = 1
    GENDER_OTHER = 2
    GENDERS = {
        GENDER_FEMALE: "Female",
        GENDER_MALE: "Male",
        GENDER_OTHER: "Other"
    }

    def __init__(self, description, sex):
        self.description = description
        self.sex = sex

    def _get_sex(self):
        return self.GENDERS[self.sex]

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)

def init_db(admin_email, admin_password):
    db.drop_all()
    db.create_all()

    # Create an admin user
    user_datastore.create_user(email=admin_email, password=admin_password)

    # Create seed data
    lorem = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    for _ in range(1, 10):
        c = Content('Description {}'.format(lorem), Content.GENDER_MALE)
        db.session.add(c)

    db.session.commit()
