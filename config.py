import os

# To generate a new secret key:
# >>> import random, string
# >>> "".join([random.choice(string.printable) for _ in range(24)])
SECRET_KEY = ";G(cVsHnI0XQCwLx/_dp=.:~"
FB_APP_ID = 1967148823570310

# LOGIN
SECURITY_PASSWORD_HASH = 'sha512_crypt'
SECURITY_PASSWORD_SALT = 'fhasdgihwntlgy8f'
SECURITY_POST_LOGIN_VIEW = '/dashboard'

WTF_CSRF_ENABLED = True

# Admin login
ADMIN_EMAIL = 'matt@nobien.net'
ADMIN_PW = 'supersuper'

# Database settings
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
MAX_WORDS = 49

if os.environ.get('DATABASE_URL') is None:
    SERVER_NAME = 'localhost:5000'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://celinems@localhost/letestultime'
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SERVER_NAME = 'le-test-ultime.herokuapp.com'
    DEBUG = True
