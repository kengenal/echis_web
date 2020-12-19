import os
from pathlib import Path


class Config(object):
    SECRET_KEY = "secret key"
    TOKEN_SECRET = os.getenv("TOKEN_SECRET", default="asdasdasd")
    TOKEN_ALGORITHM = os.getenv("TOKEN_ALGORITHM", default="HS256")


class ProdConfig(Config):
    ENV = "prod"
    MONGODB_SETTINGS = {
        "db": os.getenv("MONGO_DB"),
        "host": os.getenv("MONGO_URL")
    }


class DevConfig(Config):
    ENV = "dev"
    DEBUG = True

    MONGODB_SETTINGS = {
        "db": "admin",
        "host": "mongodb://root:example@localhost:27017/admin"
    }


class TestConfig(Config):
    ENV = "test"
    DEBUG = True
    MONGODB_SETTINGS = {
        "db": "mongoenginetest",
        "host": "mongomock://localhost"
    }
    WTF_CSRF_ENABLED = False
