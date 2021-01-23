import os


class Config(object):
    SECRET_KEY = os.getenv("SECRET_KEY", default="secret key")
    TOKEN_SECRET = os.getenv("TOKEN_SECRET", default="asdasdasd")
    TOKEN_ALGORITHM = os.getenv("TOKEN_ALGORITHM", default="HS256")
    TOKEN_LIFETIME = os.getenv("TOKEN_LIFETIME", default=1440)
    PAGINATION = 10


class ProdConfig(Config):
    ENV = "prod"
    MONGODB_SETTINGS = {
        "host": os.getenv("MONGO_URL")
    }


class DevConfig(Config):
    ENV = "dev"
    DEBUG = True

    MONGODB_SETTINGS = {
        "db": "admin",
        "host": "mongodb://root:example@mongo:27017/admin"
    }


class TestConfig(Config):
    ENV = "test"
    DEBUG = True
    MONGODB_SETTINGS = {
        "db": "mongoenginetest",
        "host": "mongomock://localhost"
    }
    WTF_CSRF_ENABLED = False
