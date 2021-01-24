from flask import request, current_app, jsonify
from flask.views import MethodView
from mongoengine import ValidationError

from echis_web.exception.exceptions import NotFoundException, BadRequestException
from echis_web.model.share_model import Playlists
from echis_web.utils.decorators import login_required_api, has_perm_api


class ApiPlaylistController(MethodView):
    decorators = [has_perm_api(permissions=["ADMIN"], methods=["POST", "PUT", "DELETE"]), login_required_api]

    @staticmethod
    def get():
        try:
            page = request.args.get("page", 1)
            playlists = Playlists.objects.paginate(page=int(page), per_page=current_app.config["PAGINATION"])
            return jsonify(res={
                "results": playlists.total,
                "page": page,
                "playlists": playlists.items
            })
        except Exception:
            raise NotFoundException()

    @staticmethod
    def post():
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
        pass

    @staticmethod
    def delete(playlist_id):
        pass
