from datetime import timedelta, datetime

import jwt


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
