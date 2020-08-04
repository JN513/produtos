from django_elasticsearch_dsl import Document, Index
from core.models import Produto, Categoria, Tipo
from elasticsearch_dsl import analyzer

produtos = Index('produtos')
categorias = Index('categorias')
tipos = Index('tipos')

html_strip = analyzer(
    'html_strip',
    tokenizer="standard",
    filter=["standard","lowercase", "stop", "snowball"],
    char_filter=["html_strip"]
)

@produtos.doc_type
class ProdutoIndex(Document):
    class Django:
        model = Produto

        fields = [
            'id','nome','descricao','slug'
        ]