from echis_web.utils.token import generate_fake_discord_token

api_login = {
    "tags": [
        "Auth"
    ],
    "security": {
        "bearerAuth": [],
    },
    "parameters": [
        {
            "name": "Authorization",
            "in": "header",
            "type": "string",
            "value": f"Bearer {generate_fake_discord_token()}",
            "default": None
        }
    ],
    "definitions": {
        "Auth": {
            "type": "object",
            "properties": {
                "token": {"type": "string"},
                "user": {
                    "type": "object",
                    "properties": {
                        "avatar": {"type": "string"},
                        "discord_id": {"type": "integer"},
                        "permissions": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            }
                        },
                        "permissions_str": {"type": "string"},
                        "public_id": {"type": "string"},
                        "username": {"type": "string"},
                    },
                }
            }
        }
    },
    "responses": {
        "200": {
            "description": "Return token and user data",
            "schema": {
                "$ref": "#/definitions/Auth"
            },
            "examples": {
                "user": {
                    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9"
                             ".eyJwdWJsaWNfaWQiOiJlNWQ2ZDJmOC03ZTgyLTQyZjEtODExOS1hMGJiNjFiNDhmMDQiLCJleHAiOjE2MTIwOTgyODN9.ET_WI7P3jOoDXvkEBeAZ8yF6zvGaXk8oeA1DpmjxnsI",
                    "user": {
                        "avatar": "https://cdn.discordapp.com/widget-avatars"
                                  "/EK8101DeRW0t0Jeze4L3YapbumoaRLCDWs5bV9Ntqf0/O7VJsYBxprw5iDc2BUlaItDtc"
                                  "-whuW9HwNy8Jm9qH-eal5gw3LhlSfTeOOqcpH0_JJSCgLWwyP9v-Nei_8kvTW-bohSs7JnQyfoUI_"
                                  "-q7osntUmM2H4LsFUPHOma1TCW2VNZqoG0x8xhmA",
                        "discord_id": 13456,
                        "permissions": [
                            "ADMIN",
                            "USER"
                        ],
                        "public_id": "e5d6d2f8-7e82-42f1-8119-a0bb61b48f04",
                        "username": "TestName"
                    }
                }
            }
        },
        "401": {
            "description": "Bad token exception",
            "schema": {
                "properties": {
                    "Error": {
                        "type": "string",
                        "description": "Invalid token",
                    }
                }
            }
        },
        "examples": {"Error": "Bad token"},
    }
}
