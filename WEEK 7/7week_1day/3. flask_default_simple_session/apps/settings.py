import os
from datetime import timedelta

# from secret_keys import CSRF_SECRET_KEY, SESSION_KEY


class Config(object):
    # Set secret keys for CSRF protection
    SECRET_KEY = "secret_keys"
    # CSRF_SESSION_KEY = SESSION_KEY
    debug = False
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=2)

class Production(Config):
    DEBUG = True
    # CSRF_ENABLED = True
    ADMIN = "lla@lla.com"