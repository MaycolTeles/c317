from django.urls import re_path

from chat.consumers import ChatConsumer


websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<room_name>\w+)/$", ChatConsumer.as_asgi()),
    # re_path(r"ws/chat/<str:session_id>", ChatConsumer.as_asgi()),
]
