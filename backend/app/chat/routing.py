from django.urls import path

from chat.consumers import ChatConsumer


websocket_urlpatterns = [
    path(r"ws/chat/<uuid:session_id>/", ChatConsumer.as_asgi()),
]
