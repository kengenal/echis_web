from flask import jsonify, current_app, request
from flask.views import MethodView
from jwt import PyJWTError
from mongoengine import ValidationError

from echis_web.exception.exceptions import BadRequestException
from echis_web.model.user_model import User
from echis_web.utils.token import decode_token, create_token


def dec(token):
    return decode_token(token=token, options={
        "TOKEN_SECRET": current_app.config["TOKEN_SECRET"],
        "TOKEN_ALGORITHM": current_app.config["TOKEN_ALGORITHM"]
    })


def create(public_id):
    return create_token(
        data={"public_id": str(public_id)},
        exp=current_app.config["TOKEN_LIFETIME"],
        options={
            "TOKEN_SECRET": current_app.config["SECRET_KEY"],
            "TOKEN_ALGORITHM": current_app.config["TOKEN_ALGORITHM"]
        }
    )


class ApiAuthController(MethodView):
    @staticmethod
    def get():
        try:
            decode = dec(token=request.headers.get("Authorization", "").replace("Barer", "").strip())
            payload = decode
            decode.pop("exp")
            payload["permissions"] = decode.get("permissions", "").upper().strip().split("|")
            user = User(**payload)
            user.validate()
            user.save()
            token = create(user.public_id)
            payload["public_id"] = user.public_id
            end_data = {"token": token, "user": payload}
            return jsonify(end_data), 200
        except ValidationError as err:
            raise BadRequestException(err.to_dict())
        except PyJWTError:
            raise BadRequestException({"Error": "Bad token"})
