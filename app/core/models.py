"""Modelo de dados"""
from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.nome)

    class Meta:
        db_table = "tb_categoria"


class Produto(models.Model):
    codigo = models.IntegerField(default=0, blank=True, null=True)
    nome = models.CharField(max_length=200, blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    preco = models.DecimalField(default=0, decimal_places=2, max_digits=10)

    def __str__(self):
        return str(self.nome)

    class Meta:
        db_table = "tb_produto"


class NotaFiscal(models.Model):
    numero = models.IntegerField(unique=True, auto_created=True)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    qnt = models.FloatField(default=0, blank=True, null=True)

    def __str__(self):
        return str(self.numero)

    class Meta:
        db_table = "tb_nota_fiscal"
