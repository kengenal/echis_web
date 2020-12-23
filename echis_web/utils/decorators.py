from functools import wraps

from flask import session, abort, redirect, url_for


def get_404():
    return abort(404)


def get_redirect(url):
    return redirect(url_for(url))


def login_required(func):
    """ if user not exist in session raise 404 """

    @wraps(func)
    def wrapper_func(*args, **kwargs):
        if "user" not in session:
            return get_404()
        return func(*args, **kwargs)

    return wrapper_func


def has_perms(perms, rd=None):
    """
    check user permission, this function get from session["permissions"] and optional url to redirect user where
    you wont if rq parameter is none decorator abord 404
    """

    def decorator(func):
        @wraps(func)
        def wrapper_func(*args, **kwargs):
            if user := session.get("user", None):
                p = user.get("permissions", None).upper()
                if not perms or perms.upper() not in p.split("|"):
                    return get_redirect(rd) if rd else get_404()
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
