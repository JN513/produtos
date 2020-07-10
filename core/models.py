from django.db import models
from datetime import datetime 
from django.contrib.auth.models import User

class Categoria(models.Model):
    nome = models.CharField(max_length=50, db_index=True)
    datetime = models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return self.nome

class Tipo(models.Model):
    nome = models.CharField(max_length=50, db_index=True)
    categoriadotipo = models.ForeignKey(Categoria , on_delete=models.CASCADE)
    datetime = models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return self.nome
class Produto(models.Model):
    nome = models.CharField(max_length=50, db_index=True)
    descricao = models.TextField()
    preco = models.IntegerField()
    quantidade = models.IntegerField()
    datadecriacao = models.DateTimeField(default=datetime.now,blank=True)
    datadefabricacao = models.DateField(max_length=20)
    criador = models.ForeignKey(User , on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria , on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
