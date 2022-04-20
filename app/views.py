import http
from flask.wrappers import Response


def respond(status: str) -> Response:
    try:
        status_code = int(status)
        if status_code not in list(http.HTTPStatus):
            raise ValueError
        return Response("", status_code)
    except ValueError:
        return Response("", 404)
