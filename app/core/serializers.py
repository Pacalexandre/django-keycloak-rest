"""Serializers"""
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from .models import Categoria, NotaFiscal, Produto


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class NotaFiscalSerializer(ModelSerializer):
    produto = PrimaryKeyRelatedField(many=True)

    class Meta:
        model = NotaFiscal
        fields = ['numero', 'produto', 'qnt']
        depth = 1


class ProdutoSerializer(ModelSerializer):
    categoria = PrimaryKeyRelatedField(many=True)

    class Meta:
        model = Produto
        fields = ['codigo', 'nome', 'categoria', 'preco']
        depth = 1
