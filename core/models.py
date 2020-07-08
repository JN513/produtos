from django.db import models
from datetime import datetime 

class Usuario(models.Model):
    nome = models.CharField(db_index=True, max_length=50,unique=True)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=200)
    username = models.CharField(max_length=25, unique=True)
    datetime = models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=50, db_index=True)
    descricao = models.TextField()
    preco = models.IntegerField()
    quantidade = models.IntegerField()
    datadecriacao = models.DateField()
    datademodificacao = models.DateField()
    criador = models.ForeignKey(Usuario , on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria , on_delete=models.CASCADE)
    tipo = models.ManyToManyField(Tipo)

class Categoria(models.Model):
    nome = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return self.nome

class Tipo(models.Model):
    nome = models.CharField(max_length=50, db_index=True)
    Categoria = models.ForeignKey(Categoria , on_delete=models.CASCADE)