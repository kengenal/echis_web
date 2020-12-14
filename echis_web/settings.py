import os
from pathlib import Path


class Config(object):
    SECRET_KEY = "secret key"
    TOKEN_SECRET = os.getenv("TOKEN_SECRET", default="asdasdasd")
    TOKEN_ALGORITHM = os.getenv("TOKEN_ALGORITHM", default="HS256")
    SESSION_TYPE = "filesystem"
    BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent
    SESSION_FILE_DIR = os.path.join(BASE_DIR, "sessions")


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
        "db": "mongoenginetest",
        "host": "mongomock://localhost"
    }

    CACHE_TYPE = "null"
    ASSETS_DEBUG = True


class TestConfig(Config):
    ENV = "test"
    DEBUG = True
    MONGODB_SETTINGS = {
        "db": "mongoenginetest",
        "host": "mongomock://localhost"
    }
    WTF_CSRF_ENABLED = False
