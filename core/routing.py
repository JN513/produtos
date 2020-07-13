from django.urls import re_path
from channels.routing import route
from core.consumers import ws_connect, ws_disconnect

from . import consumers

websocket_urlpatterns = [
    #re_path(r'ws/core/(?P<room_name>\w+)/$', consumers.LiveProdutos),
    route('websocket.connect', ws_connect),
    route('websocket.disconnect', ws_disconnect),
]
