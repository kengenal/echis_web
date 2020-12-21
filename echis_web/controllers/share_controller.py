from flask import Blueprint, request, render_template, session, redirect, url_for, flash
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
@has_perms("ADMIN", rd="share.get_playlists")
def create_playlist():
    playlist_form = model_form(Playlists)
    form = playlist_form(request.form)
    if request.method == "POST" and form.validate():
        form.user = session["user"]["username"]
        form.save()
        return redirect(url_for("share.get_playlists"))
    return render_template("share/new.html", form=form)


@share.route("playlists/<string:pl_id>/edit", methods=["POST", "GET"])
@login_required
@has_perms("ADMIN", rd="share.get_playlists")
def edit_playlist(pl_id):
    playlist = Playlists.objects.get_or_404(playlist_id=pl_id)
    playlist_form = model_form(Playlists)
    form = playlist_form(request.form)
    if request.method == "POST" and form.validate():
        pl = form.data.get("playlist_id", playlist.playlist_id)
        playlist.playlist_id = pl
        playlist.api = form.data.get("api", playlist.api)
        playlist.is_active = form.data.get("is_active", playlist.is_active)
        playlist.save()
        flash(f"Playlist {pl} has been updated", "success")
        return redirect(url_for("share.get_playlists"))
    return render_template("share/edit_playlist.html", form=form, playlist=playlist)


@share.route("playlists/<string:playlist_id>/delete", methods=["GET"])
@login_required
@has_perms("ADMIN", rd="share.get_playlists")
def delete_playlist(playlist_id):
    playlist = Playlists.objects.get_or_404(playlist_id=playlist_id)
    playlist.delete()
    flash("Playlist has been removed", "success")

    return redirect(url_for("share.get_playlists"))
