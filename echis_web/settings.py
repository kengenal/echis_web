import os


class SwaggerConfig:
    SWAGGER_TEMPLATE = {
        "info": {
            "title": "Echis web docs",
            "version": "1.0",
        },
        "components": {
            "securitySchemes": {
                "bearerAuth": {
                    "type": "http",
                    "scheme": "bearer",
                    "bearerFormat": "JWT",
                    "description": "Token"
                }
            }
        },
        "produces": [
            "application/json",
        ],
        "security: {bearerAuth": [],
    }
    SWAGGER_CONFIG = {
        "headers": [
        ],
        "specs": [
            {
                "endpoint": 'apispec_1',
                "route": '/apispec_1.json',
                "rule_filter": lambda rule: True,  # all in
                "model_filter": lambda tag: True,  # all in
            }
        ],
        "static_url_path": "/api/flasgger_static",
        "swagger_ui": True,
        "title": "Echis web docs",
        "specs_route": "/api/docs"
    }


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", default="dlfmlsdk,mfl';ksdmflk;sdm")
    TOKEN_SECRET = os.getenv("TOKEN_SECRET", default="asdasdasd")
    TOKEN_ALGORITHM = os.getenv("TOKEN_ALGORITHM", default="HS256")
    TOKEN_LIFETIME = os.getenv("TOKEN_LIFETIME", default=1440)
    PAGINATION = 10
    API_AVAILABLE = ["spotify", "deezer", "youtube", "apple_music"]


class ProdConfig(Config):
    ENV = "prod"
    MONGODB_SETTINGS = {
        "host": os.getenv("MONGO_URL")
    }


class DevConfig(Config, SwaggerConfig):
    ENV = "dev"
    DEBUG = True

    MONGODB_SETTINGS = {
        "db": "admin",
        "host": os.getenv("MONGO_URL")
    }


class TestConfig(Config):
    ENV = "test"
    DEBUG = True
    MONGODB_SETTINGS = {
        "db": "mongoenginetest",
        "host": "mongomock://localhost"
    }
    WTF_CSRF_ENABLED = False
