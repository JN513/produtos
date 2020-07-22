from datetime import datetime
from elasticsearch_dsl import Document, Date, Keyword, Text
from elasticsearch_dsl.connections import connections
from . import models

connections.create_connection(hosts=['localhost'])

class ProdutoIndex(Document):
    nome = Text()
    descricao = Text()
    preco = Text()
    quantidade = Text()
    datadecriacao = Date()
    datadefabricacao = Date()
    criador = Text()
    categoria = Text()
    tipo = Text()

    class Index:        
        name = 'produto'

ProdutoIndex.init()
