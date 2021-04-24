from echis_web.exception.exceptions import NotFoundException, BadRequestException
from echis_web.model.filter_model import FilterModel
from echis_web.utils.decorators import has_perm_api, login_required_api
from flask.views import MethodView
from flask import jsonify, request
from mongoengine import ValidationError, NotUniqueError


class ApiFilterController(MethodView):
    has_perm_for_methods = ["POST", "PUT", "DELETE"]
    decorators = [has_perm_api(permissions=["ADMIN"], methods=has_perm_for_methods), login_required_api]

    @staticmethod
    def get():
        """
        file: docs/filter/get_playlists_items.yaml
        """
        try:
            filter_items = FilterModel.objects.on.all()
            return jsonify(filter_items)
        except Exception:
            raise NotFoundException()

    @staticmethod
    def post():
        """
        file: docs/filter/create_item.yaml
        """
        rq = request.get_json()
        try:
            if rq:
                words = set(rq.get("words"))
                if not words:
                    raise ValidationError(errors={"words": "Cannot be empty"})
                created_words = []
                for name in words:
                    new_filter = FilterModel(name=name)
                    new_filter.validate()
                    new_filter.save()
                    created_words.append(new_filter)
                return jsonify(created_words), 201
            raise ValidationError(errors={"words": "Cannot be empty"})
        except ValidationError as err:
            raise BadRequestException(err.to_dict())
        except TypeError:
            raise BadRequestException({"words": "Cannot be empty"})
        except NotUniqueError:
            raise BadRequestException({"words": "Word already exist"})

    @staticmethod
    def delete(word_id):
        """
        file: docs/filter/delete_item.yaml
        """
        try:
            playlist = FilterModel.objects.get_or_404(pk=word_id)
            playlist.delete()
            return jsonify({"Success": "Playlist has been removed"}), 204
        except Exception:
            raise NotFoundException()
