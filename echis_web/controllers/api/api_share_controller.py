from flask import request, current_app, jsonify
from flask.views import MethodView
from mongoengine import ValidationError

from echis_web.exception.exceptions import NotFoundException, BadRequestException
from echis_web.model.share_model import Playlists, SharedSongs
from echis_web.utils.decorators import login_required_api, has_perm_api


class ApiPlaylistController(MethodView):
    has_perm_for_methods = ["POST", "PUT", "DELETE"]
    decorators = [has_perm_api(permissions=["ADMIN"], methods=has_perm_for_methods), login_required_api]

    def get(self, page=1):
        """
        file: docs/playlists/get_playlists_items.yaml
        """
        try:
            playlists = Playlists.objects.paginate(page=page, per_page=current_app.config["PAGINATION"])
            return jsonify({
                "results": playlists.total,
                "page": page,
                "has_admin": self.has_perm_for_methods,
                "playlists": playlists.items,
                "api_available": current_app.config["API_AVAILABLE"]
            })
        except Exception:
            raise NotFoundException()

    @staticmethod
    def post():
        """
        file: docs/playlists/create_item.yaml
        """
        rq = request.get_json()
        try:
            playlist = Playlists(**rq)
            playlist.validate()
            playlist.save()
            return jsonify(playlist.to_json()), 201
        except ValidationError as err:
            raise BadRequestException(err.to_dict())

    @staticmethod
    def put(playlist_id):
        """
        file: docs/playlists/update_item.yaml
        """
        try:
            active = request.get_json().get('is_active')
            if active is not None:
                playlist = Playlists.objects.get_or_404(playlist_id=playlist_id)
                playlist.update(
                    set__is_active=active,
                )
                return jsonify(playlist.to_json())
            raise ValidationError(field_name="is_active", message="Cannot be empty")
        except ValidationError as err:
            raise BadRequestException(err.to_dict())
        except Exception:
            raise NotFoundException()

    @staticmethod
    def delete(playlist_id):
        """
        file: docs/playlists/delete_item.yaml
        """
        try:
            playlist = Playlists.objects.get_or_404(playlist_id=playlist_id)
            playlist.delete()
            return jsonify({"Error": "Playlist has been removed"}), 204
        except Exception:
            raise NotFoundException()


class ApiSongController(MethodView):
    has_perm_for_methods = ["DELETE"]
    decorators = [has_perm_api(permissions=["ADMIN"], methods=has_perm_for_methods), login_required_api]

    def get(self, page=1):
        """
        file: docs/songs/get_items.yaml
        """
        try:
            songs = SharedSongs.objects.paginate(page=page, per_page=current_app.config["PAGINATION"])
            return jsonify({
                "results": songs.total,
                "page": page,
                "has_admin": self.has_perm_for_methods,
                "songs": songs.items,
            })
        except Exception:
            raise NotFoundException()

    @staticmethod
    def delete(record_id):
        """
        file: docs/songs/delete_item.yaml
        """
        try:
            song = SharedSongs.objects.get_or_404(record_id=record_id)
            song.delete()
            return jsonify({"Error": "Song has been removed"}), 204
        except Exception:
            raise NotFoundException()
