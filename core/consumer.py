# Built in imports.
import json
# Third Party imports.
from channels.exceptions import DenyConnection
from channels.generic.websocket import AsyncWebsocketConsumer
# Django imports.
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import AnonymousUser
# Local imports.
from core.models import Produto, Categoria, Tipo

class LiveProdutos(AsyncWebsocketConsumer):
    def connect(self):
        self.accept()
    
    def disconnect(self, close_code):
        pass