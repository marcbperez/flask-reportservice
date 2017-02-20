import os


class base_config(object):
    SECRET_KEY = os.environ['SECRET_KEY']

    POSTGRES_HOST = os.environ['DB_HOST']
    POSTGRES_PORT = os.environ['DB_PORT']
    POSTGRES_USER = os.environ['DB_USER']
    POSTGRES_PASS = os.environ['DB_PASS']
    POSTGRES_DB = os.environ['DB_NAME']

    SQLALCHEMY_DATABASE_URI = 'postgresql://%s:%s@%s:%s/%s' % (
        POSTGRES_USER,
        POSTGRES_PASS,
        POSTGRES_HOST,
        POSTGRES_PORT,
        POSTGRES_DB
    )


class dev_config(base_config):
    DEBUG = True
    ASSETS_DEBUG = True
    WTF_CSRF_ENABLED = False


class test_config(base_config):
    TESTING = True
    WTF_CSRF_ENABLED = False
