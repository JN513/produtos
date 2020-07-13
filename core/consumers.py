from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import AnonymousUser
from core.models import Produto, Categoria, Tipo


class LiveProdutos(AsyncWebsocketConsumer):
    def ws_connect(self):
        self.accept()
    
    def ws_receive(self):
        pass

    def wsdisconnect(self, close_code):
        pass

