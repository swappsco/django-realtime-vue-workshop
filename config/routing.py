from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

# from idk.notifications import routing
from workshop.surveys import routing

application = ProtocolTypeRouter(
    {"websocket": AuthMiddlewareStack(URLRouter(routing.websocket_urlpatterns))}
)
