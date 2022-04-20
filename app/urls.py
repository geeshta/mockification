from app import server
from . import views

server.add_url_rule("/respond/<status>", view_func=views.respond)
