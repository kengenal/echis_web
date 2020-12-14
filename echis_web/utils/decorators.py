from functools import wraps
from flask import session, abort


def get_404():
    return abort(404)


def login_required(func):
    """ if user not exist in session raise 404 """
    @wraps(func)
    def wrapper_func(*args, **kwargs):
        if "user" not in session:
            return get_404()
        return func(*args, **kwargs)
    return wrapper_func


def has_perms(perms):
    """ check user permission, this function get from session["permissions"] """
    def decorator(func):
        @wraps(func)
        def wrapper_func(*args, **kwargs):
            if user := session.get("user", None):
                p = user.get("permissions", None)
                if not perms or perms not in p.split("|"):
                    return get_404()
            else:
                return get_404()
            return func(*args, **kwargs)
        return wrapper_func
    return decorator


def unauthorized(func):
    @wraps(func)
    def wrapper_func(*args, **kwargs):
        if "user" in session:
            return get_404()
        return func(*args, **kwargs)
    return wrapper_func
