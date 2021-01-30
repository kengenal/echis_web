from datetime import timedelta, datetime

import jwt

from echis_web.settings import DevConfig


def generate_fake_discord_token():
    """ create token to login with dami data """

    config = DevConfig()
    prepare_data = {
        "permissions": "ADMIN|USER",
        "username": "TestName",
        "discord_id": 13456,
        "avatar": "https://cdn.discordapp.com/widget-avatars/EK8101DeRW0t0Jeze4L3YapbumoaRLCDWs5bV9Ntqf0"
                  "/O7VJsYBxprw5iDc2BUlaItDtc-whuW9HwNy8Jm9qH-eal5gw3LhlSfTeOOqcpH0_JJSCgLWwyP9v-Nei_8kvTW"
                  "-bohSs7JnQyfoUI_-q7osntUmM2H4LsFUPHOma1TCW2VNZqoG0x8xhmA",
    }
    return create_token(data=prepare_data, options={
        "TOKEN_SECRET": config.TOKEN_SECRET,
        "TOKEN_ALGORITHM": config.TOKEN_ALGORITHM
    })


def create_token(data, exp=50, options=None):
    if options is None:
        options = {}
    get_secret = options.get("TOKEN_SECRET", "asdasdasd")
    get_alg = options.get("TOKEN_ALGORITHM", "HS256")
    payload = data
    if not data:
        raise Exception("Data cannot be null")
    payload["exp"] = datetime.utcnow() + timedelta(minutes=exp)
    token = jwt.encode(payload, get_secret, algorithm=get_alg).decode("UTF-8")
    return token


def decode_token(token, options=None):
    if options is None:
        options = {}
    get_secret = options.get("TOKEN_SECRET", "asdasdasd")
    get_alg = options.get("TOKEN_ALGORITHM", "HS256")
    data = jwt.decode(bytes(token, encoding="utf8"), get_secret, algorithms=[get_alg])
    return data
