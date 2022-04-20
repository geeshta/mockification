from flask.wrappers import Response


def respond(status: str) -> Response:
    try:
        status_code = int(status)
        return Response("", status_code)
    except ValueError:
        return Response("", 404)
