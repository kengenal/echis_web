from flask import Blueprint, current_app, abort, redirect, url_for

from echis_web.extensions import sess
from echis_web.forms.auth_form import AuthForm
from echis_web.utils.token import decode_token

auth = Blueprint("auth", __name__, url_prefix="/auth")


@auth.route("/<token>", methods=["GET"])
def login(token: str):
    try:
        decode = decode_token(token=token, options={
            "TOKEN_SECRET": current_app.config["TOKEN_SECRET"],
            "TOKEN_ALGORITHM": current_app.config["TOKEN_ALGORITHM"]
        })
        form = AuthForm(data=decode)
        if form.validate():
            sess["user"] = decode
            return redirect(url_for("home.index"))
        abort(404)
    except Exception:
        abort(404)


@auth.route("/logout")
def logout():
    # remove the username from the session if it's there
    sess.pop("user", None)
    abort(404)

