from flask import Blueprint

auth = Blueprint("auth", __name__, url_prefix="/auth")


@auth.route("/<token>", methods=["GET"])
def login(token: str):
    return "asdasd"
