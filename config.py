import os

# To generate a new secret key:
# >>> import random, string
# >>> "".join([random.choice(string.printable) for _ in range(24)])
SECRET_KEY = ";G(cVsHnI0XQCwLx/_dp=.:~"

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
MAX_WORDS = 49

# local
if os.environ.get('DATABASE_URL') is None:
    BASE_URL = 'localhost:5000'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    #SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://celinems@localhost/letestultime'
    FB_APP_ID = 1200420960103822
# heroku
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    BASE_URL = 'https://le-test-ultime.herokuapp.com'
    FB_APP_ID = 1967148823570310
