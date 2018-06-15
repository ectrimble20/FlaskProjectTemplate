import os
from datetime import timedelta
import logging


class Config(object):
    """
    Default configuration object.  This object contains default values pulled from the Flask documentation.
    It does not extend into other configurations such as SQLAlchemy or other lib, just Flask itself.

    All the parameters are prefixed with FLASK_SVC_***

    To add the parameters to your environment (to allow Flask to load them) you'll need to use the EXPORT
    command on Linux/Mac or the SET command on windows

    If you don't know how to do this, I suggest Google as this isn't a tutorial.
    """
    ENV = os.environ.get('FLASK_SVC_ENV', 'production')
    DEBUG = os.environ.get('FLASK_SVC_DEBUG', False)
    TESTING = os.environ.get('FLASK_SVC_TESTING', False)
    PROPAGATE_EXCEPTIONS = os.environ.get('FLASK_SVC_PROPAGATE_EXCEPTIONS', None)
    PRESERVE_CONTEXT_ON_EXCEPTION = os.environ.get('FLASK_SVC_PRESERVE_CONTEXT_ON_EXCEPTION', None)
    TRAP_HTTP_EXCEPTIONS = os.environ.get('FLASK_SVC_TRAP_HTTP_EXCEPTIONS', False)
    TRAP_BAD_REQUEST_ERRORS = os.environ.get('FLASK_SVC_TRAP_BAD_REQUEST_ERRORS', None)
    SECRET_KEY = os.environ.get('FLASK_SVC_SECRET_KEY', None)
    SESSION_COOKIE_NAME = os.environ.get('FLASK_SVC_SESSION_COOKIE_NAME', 'session')
    SESSION_COOKIE_DOMAIN = os.environ.get('FLASK_SVC_SESSION_COOKIE_DOMAIN', None)
    SESSION_COOKIE_PATH = os.environ.get('FLASK_SVC_SESSION_COOKIE_PATH', None)
    SESSION_COOKIE_HTTPONLY = os.environ.get('FLASK_SVC_SESSION_COOKIE_HTTPONLY', True)
    SESSION_COOKIE_SECURE = os.environ.get('FLASK_SVC_SESSION_COOKIE_SECURE', False)
    SESSION_COOKIE_SAMESITE = os.environ.get('FLASK_SVC_SESSION_COOKIE_SAMESITE', None)
    PERMANENT_SESSION_LIFETIME = os.environ.get('FLASK_SVC_PERMANENT_SESSION_LIFETIME', timedelta(days=32))
    SESSION_REFRESH_EACH_REQUEST = os.environ.get('FLASK_SVC_SESSION_REFRESH_EACH_REQUEST', True)
    USE_X_SENDFILE = os.environ.get('FLASK_SVC_USE_X_SENDFILE', False)
    SEND_FILE_MAX_AGE_DEFAULT = os.environ.get('FLASK_SVC_SEND_FILE_MAX_AGE_DEFAULT', timedelta(hours=12))
    SERVER_NAME = os.environ.get('FLASK_SVC_SERVER_NAME', None)
    APPLICATION_ROOT = os.environ.get('FLASK_SVC_APPLICATION_ROOT', '/')
    PREFERRED_URL_SCHEME = os.environ.get('FLASK_SVC_PREFERRED_URL_SCHEME', 'http')
    MAX_CONTENT_LENGTH = os.environ.get('FLASK_SVC_MAX_CONTENT_LENGTH', None)
    JSON_AS_ASCII = os.environ.get('FLASK_SVC_JSON_AS_ASCII', True)
    JSON_SORT_KEYS = os.environ.get('FLASK_SVC_JSON_SORT_KEYS', True)
    JSONIFY_PRETTYPRINT_REGULAR = os.environ.get('FLASK_SVC_JSONIFY_PRETTYPRINT_REGULAR', False)
    JSONIFY_MIMETYPE = os.environ.get('FLASK_SVC_JSONIFY_MIMETYPE', 'application/json')
    TEMPLATES_AUTO_RELOAD = os.environ.get('FLASK_SVC_TEMPLATES_AUTO_RELOAD', None)
    EXPLAIN_TEMPLATE_LOADING = os.environ.get('FLASK_SVC_EXPLAIN_TEMPLATE_LOADING', False)
    MAX_COOKIE_SIZE = os.environ.get('FLASK_SVC_MAX_COOKIE_SIZE', 4093)
    SQLALCHEMY_DATABASE_URI = os.environ.get('FLASK_SVC_DB_URI')
    HOST = os.environ.get('FLASK_SVC_HOST', 'localhost')
    LOGGING_FILE = os.environ.get('FLASK_SVC_LOG', 'application.log')
    LOGGING_LEVEL = os.environ.get('FLASK_SVC_LOG_LEVEL', logging.ERROR)
