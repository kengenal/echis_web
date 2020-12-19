from flask import Blueprint, request, render_template, session, redirect, url_for
from flask_mongoengine.wtf import model_form

from echis_web.model.share_model import Playlists
from echis_web.utils.decorators import login_required, has_perms

share = Blueprint("share", __name__, url_prefix="/share")


@share.route("/playlists", methods=["GET"])
@login_required
def get_playlists():
    page = request.args.get("page", 1)
    playlists = Playlists.objects.paginate(page=int(page), per_page=1)

    return render_template("share/playlists.html", playlists=playlists)


@share.route("/playlists/new", methods=["POST", "GET"])
@login_required
@has_perms("ADMIN")
def create_playlist():
    playlist_form = model_form(Playlists)
    form = playlist_form(request.form)
    if request.method == "POST" and form.validate():
        form.user = session["user"]["username"]
        form.save()
        # return redirect(url_for("share.get_playlists"))
    return render_template("share/new.html", form=form)
