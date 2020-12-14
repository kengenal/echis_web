from flask import Blueprint, render_template

from echis_web.utils.decorators import login_required

home = Blueprint("home", __name__)


@home.route("/home", methods=["GET"])
@login_required
def index():
    return render_template("home/index.html")
