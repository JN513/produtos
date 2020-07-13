from channels.exceptions import DenyConnection
from channels.generic.websocket import AsyncWebsocketConsumer
from channels import Group
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import AnonymousUser
from core.models import Produto, Categoria, Tipo

"""
class LiveProdutos(AsyncWebsocketConsumer):
    def connect(self):
        self.accept()
    
    def disconnect(self, close_code):
        pass

"""

def ws_connect(message):
    Group('users').add(message.reply_channel)


def ws_disconnect(message):
    Group('users').discard(message.reply_channel)   