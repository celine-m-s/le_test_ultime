import os

# To generate a new secret key:
# >>> import random, string
# >>> "".join([random.choice(string.printable) for _ in range(24)])
SECRET_KEY = ";G(cVsHnI0XQCwLx/_dp=.:~"
DEBUG = True
TESTING = True
LIVESERVER_PORT = 8943
LIVESERVER_TIMEOUT = 10
SERVER_NAME = 'localhost:8943'
WTF_CSRF_ENABLED = True

# Administration area
SECURITY_PASSWORD_HASH = 'sha512_crypt'
SECURITY_PASSWORD_SALT = 'fhasdgihwntlgy8f'
SECURITY_POST_LOGIN_VIEW = '/dashboard'

# Admin login
ADMIN_EMAIL = 'matt@nobien.net'
ADMIN_PW = 'supersuper'

# Database settings
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app_test.db')

# Facebook settings
FB_APP_ID = 1200420960103822
FB_FIRST_NAME = 'Ellen'
FB_PASSWORD = 'YOLOYOLO'
FB_EMAIL = 'ellen_rmilrcp_page@tfbnw.net'
FB_USER_ID = '104172243553255'
FB_USER_GENDER = 'female'
