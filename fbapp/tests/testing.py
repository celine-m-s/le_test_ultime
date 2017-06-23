import os

# To generate a new secret key:
# >>> import random, string
# >>> "".join([random.choice(string.printable) for _ in range(24)])
SECRET_KEY = ";G(cVsHnI0XQCwLx/_dp=.:~"
FB_APP_ID = 1967148823570310
TESTING = True
LIVESERVER_PORT = 8943
LIVESERVER_TIMEOUT = 10
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

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app_test.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

MAX_WORDS = 49

BASE_URL = 'localhost:8943'

FB_USER = 'Tom Hanks'
FB_FIRST_NAME = 'Tom'
FB_PASSWORD = 'vendredi'
FB_EMAIL = 'tom_orfxthk_hanks@tfbnw.net'

DEBUG = True
