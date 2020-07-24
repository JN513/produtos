from django_elasticsearch_dsl import Document, Index
from core.models import Produto, Categoria, Tipo

produtos = Index('produtos')
categorias = Index('categorias')
tipos = Index('tipos')

@produtos.doc_type
class ProdutoIndex(Document):
    class Django:
        model = Produto

        fields = [
            'id','nome','descricao','slug'
        ]