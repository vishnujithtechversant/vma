import os

FB_AUTHORIZATION_BASE_URL = "https://www.facebook.com/dialog/oauth"
FB_TOKEN_URL = "https://graph.facebook.com/oauth/access_token"
BASE_URL = "https://035d8ee0.ngrok.io"

class BaseConfig:
    """Base configuration"""
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'mysecretkey')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PARENT_BASE_URL = os.environ.get("PARENT_BASE_URL")


class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    FB_CLIENT_ID = os.environ.get('FB_CLIENT_ID','1368492610005815')
    FB_CLIENT_SECRET = os.environ.get('FB_CLIENT_SECRET', '51a4a2909b26a69fa2e6fbc132fc4b43')
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(BaseConfig):
    """Testing configuration"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_TEST_URL')


class StagingConfig(BaseConfig):
    """Staging configuration"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class ProductionConfig(BaseConfig):
    """Production configuration"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
