"""Serializers"""
from rest_framework.serializers import ModelSerializer
from .models import Categoria, NotaFiscal, Produto


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class NotaFiscalSerializer(ModelSerializer):
    class Meta:
        model = NotaFiscal
        fields = '__all__'


class ProdutoSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'
