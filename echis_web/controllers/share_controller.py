from flask import Blueprint, request, render_template, session, redirect, url_for, flash, current_app, abort
from flask_mongoengine.wtf import model_form

from echis_web.model.share_model import Playlists, SharedSongs
from echis_web.utils.decorators import login_required, has_perms

share = Blueprint("share", __name__, url_prefix="/share")


@share.route("/playlists", methods=["GET"])
@login_required
def get_playlists():
    try:
        page = request.args.get("page", 1)
        playlists = Playlists.objects.paginate(page=int(page), per_page=current_app.config["PAGINATION"])
        return render_template("share/playlists.html", playlists=playlists)
    except Exception:
        abort(404)


@share.route("/playlists/new", methods=["POST", "GET"])
@login_required
@has_perms("ADMIN", rd="share.get_playlists")
def create_playlist():
    playlist_form = model_form(Playlists)
    form = playlist_form(request.form)
    if request.method == "POST" and form.validate():
        playlist = Playlists(
            user=session["user"]["username"],
            playlist_id=form.playlist_id.data,
            api=form.api.data,
            is_active=form.is_active.data
        )
        playlist.save()
        flash("Playlist has been added", "success")
        return redirect(url_for("share.get_playlists"))
    return render_template("share/new.html", form=form)


@share.route("playlists/<string:playlist_id>/edit", methods=["POST", "GET"])
@login_required
@has_perms("ADMIN", rd="share.get_playlists")
def edit_playlist(playlist_id):
    playlist = Playlists.objects.get_or_404(playlist_id=playlist_id)
    playlist_form = model_form(Playlists)
    form = playlist_form(request.form)
    if request.method == "POST" and form.validate():
        pl = form.playlist_id.data
        playlist.playlist_id = str(pl)
        playlist.api = form.api.data
        playlist.is_active = form.is_active.data
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


@share.route("/songs", methods=["GET"])
@login_required
def get_songs():
    page = request.args.get("page", 1)
    songs = SharedSongs.objects.paginate(page=int(page), per_page=current_app.config["PAGINATION"])

    return render_template("share/songs.html", songs=songs)


@share.route("songs/<uuid:record_id>/delete", methods=["GET"])
@login_required
@has_perms("ADMIN", rd="share.get_songs")
def delete_song(record_id):
    songs = SharedSongs.objects.get_or_404(record_id=record_id)
    songs.delete()
    flash("Song has been removed", "success")

    return redirect(url_for("share.get_songs"))
