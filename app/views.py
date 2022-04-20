import http
from flask import url_for
from flask.wrappers import Response


def respond(status: str) -> Response:
    try:
        status_code = int(status)
        if status_code not in list(http.HTTPStatus):
            raise ValueError
        response = Response("", status_code)
        if 300 <= status_code < 400:
            print("setting status")
            response.headers["Location"] = url_for("respond", status=200)
        return response
    except ValueError:
        return Response("", 404)
