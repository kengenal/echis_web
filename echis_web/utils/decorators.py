from functools import wraps

import jwt
from flask import abort, redirect, url_for, request, g

from echis_web.exception.exceptions import UnauthorizedException, ForbiddenException
from echis_web.model.user_model import User
from echis_web.utils.token import token_app_decoder


def get_404():
    return abort(404)


def get_redirect(url):
    return redirect(url_for(url))


def login_required_api(func):
    """ if user not exist in session raise 404 """

    @wraps(func)
    def wrapper_func(*args, **kwargs):
        try:
            token_decode = token_app_decoder()
            get_user = User.get_user_or_rise_exception(public_id=token_decode.get("public_id", None))
            g.user = get_user
        except jwt.PyJWTError:
            raise UnauthorizedException()
        except Exception:
            raise UnauthorizedException()
        return func(*args, **kwargs)

    return wrapper_func


def has_perm_api(permissions=None, methods=None):
    """ Check user permissions if user don't have permission raise ForbiddenException """
    if permissions is None:
        permissions = []
    if methods is None:
        methods = []

    def decorator(func):
        @wraps(func)
        def wrapper_func(*args, **kwargs):
            user = g.user
            if request.method in methods or not methods:
                perms = [x for x in permissions if user.has_perm(x) is True]
                if len(perms) == 0:
                    raise ForbiddenException()
            return func(*args, **kwargs)

        return wrapper_func

    return decorator
