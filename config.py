import os

SECRET_KEY = os.environ.get('SECRET_KEY', ";G(cVsHnI0XQCwLx/_dp=.:~")

# Login settings
SECURITY_PASSWORD_HASH = 'bcrypt'
SECURITY_PASSWORD_SALT = os.environ.get('SECURITY_PASSWORD_SALT', 'fhasdgihwntlgy8f')
SECURITY_POST_LOGIN_VIEW = '/dashboard'

WTF_CSRF_ENABLED = True

# Administration area
ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL', 'fantomette@hello-birds.com')
ADMIN_PW = os.environ.get('ADMIN_PW', 'catseyes')

# Database settings
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///' + os.path.join(basedir, 'app.db'))

# Facebook
FB_APP_ID = os.environ.get('FB_APP_ID', 1200420960103822)
