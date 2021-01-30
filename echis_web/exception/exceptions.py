class HttpBaseException(Exception):
    message = None

    def __init__(self, payload=None):
        Exception.__init__(self)
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or {})
        if self.message:
            rv["message"] = self.message
        return rv


class UnauthorizedException(HttpBaseException):
    status_code = 401
    message = "User not exists"


class ForbiddenException(HttpBaseException):
    status_code = 403
    message = "You don't has permission"


class BadRequestException(HttpBaseException):
    status_code = 400


class NotFoundException(HttpBaseException):
    status_code = 404
    message = "Page not found"
