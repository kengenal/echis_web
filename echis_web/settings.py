

class Config(object):
    SECRET_KEY = "secret key"


class ProdConfig(Config):
    ENV = "prod"
    MONGODB_SETTINGS = {
        "db": "project1",
        "host": "mongodb://localhost/database_name"
    }


class DevConfig(Config):
    ENV = "dev"
    DEBUG = True

    MONGODB_SETTINGS = {
        "db": "project1",
        "host": "mongodb://localhost/database_name"
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
