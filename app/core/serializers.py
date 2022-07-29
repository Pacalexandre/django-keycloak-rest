"""Serializers"""
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from .models import Categoria, NotaFiscal, Produto


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class ProdutoSerializer(ModelSerializer):
    categoria = PrimaryKeyRelatedField(
        queryset=Categoria.objects.all(), many=False)

    class Meta:
        model = Produto
        fields = ['codigo', 'nome', 'categoria', 'preco']
        depth = 1


class ProdutoListSerializer(ModelSerializer):
    categoria = CategoriaSerializer()

    class Meta:
        model = Produto
        fields = ['codigo', 'nome', 'categoria', 'preco']
        depth = 1


class NotaFiscalSerializer(ModelSerializer):
    produto = PrimaryKeyRelatedField(
        queryset=Produto.objects.all(), many=False)

    class Meta:
        model = NotaFiscal
        fields = ['numero', 'produto', 'qnt']
        depth = 1
