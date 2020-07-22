from datetime import datetime
from elasticsearch_dsl import Document, Date, Keyword, Text, DocType
from elasticsearch_dsl.connections import connections
from core.models import Produto, Categoria, Tipo

connections.create_connection(hosts=['localhost:9200'])

class ProdutoIndex(DocType):
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

    def  get_model (self):
        return  Produto
    
    def get_index_queryset(self):
        return self.get_model()

    def get_updated_field(self):
        return 'datadecriacao'

    def is_published(self):
        return datetime.now() >= self.datadecriacao

    def prepare_tags(self):
        values = self.obj.tags.all().values_list('nome', flat=True)
        return ", ".join(values)

    def create_document_dict(self, obj):
        self.obj = obj

        doc = ProdutoIndex(
            nome=obj.nome,
            descricao=obj.descricao,
            preco=obj.preco,
            quantidade=obj.quantidade,
            datadecriacao=obj.datadecriacao,
            datadefabricacao=obj.datadefabricacao,
            criador=obj.criador,
            categoria=obj.categoria,
            tipo=obj.tipo,
        )
        doc.meta.id = obj.id
        return doc.to_dict(include_meta=True)

ProdutoIndex.init()
