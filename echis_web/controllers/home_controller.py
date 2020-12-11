from flask import Blueprint

home = Blueprint("home", __name__)


@home.route("/home", methods=["GET"])
def index():
    return "hello world"
