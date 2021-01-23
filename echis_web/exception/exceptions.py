class HttpBaseException(Exception):
    def __init__(self, message=None, payload=None):
        Exception.__init__(self)
        self.message = message
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


class UnauthorizedException(HttpBaseException):
    status_code = 401
    message = "User not exists"


class ForbiddenException(HttpBaseException):
    status_code = 403
    message = "You don't has permission"
