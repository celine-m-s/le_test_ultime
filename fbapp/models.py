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
    GENDER_FEMALE = 0
    GENDER_MALE = 1
    GENDER_OTHER = 2
    GENDERS = {
        GENDER_FEMALE: "Female",
        GENDER_MALE: "Male",
        GENDER_OTHER: "Other"
    }

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200))
    gender = db.Column('gender', db.Integer, nullable=False, default=GENDER_MALE)

    def __init__(self, description, gender):
        self.description = description
        self.gender = gender

    def _get_gender(self):
        return self.GENDERS[self.gender]


# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)


def init_db(admin_email, admin_password):
    db.drop_all()
    db.create_all()

    # Create an admin user
    user_datastore.create_user(email=admin_email, password=admin_password)

    # Create seed data
    db.session.add(Content("What's your favorite scary movie?", Content.GENDER_MALE))
    db.session.add(Content("THIS IS SPARTAAAAAAAAAAAAAAAAAAA", Content.GENDER_FEMALE))

    db.session.commit()
