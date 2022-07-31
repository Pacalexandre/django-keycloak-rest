"""Serializers"""
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from .services import MontaCalculoImposto
from .models import Categoria, NotaFiscal, Produto



class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class ProdutoSerializer(ModelSerializer):
    categoria = CategoriaSerializer(many=False)
    class Meta:
        model = Produto
        fields = '__all__'
        depth = 1


class ProdutoCreateSerializer(ModelSerializer):
    categoria = PrimaryKeyRelatedField(queryset = Categoria.objects.all(),many=False)
    class Meta:
        model = Produto
        fields = '__all__'
        depth = 1


class NotaFiscalSerializer(ModelSerializer):
    produto = PrimaryKeyRelatedField(
        queryset=Produto.objects.all(), many=False)

    class Meta:
        model = NotaFiscal
        fields = '__all__'
        depth = 1

    def create(self, validated_data):
        data=validated_data.copy()
        MontaCalculoImposto().carrega_dados(data)
        return super().create(validated_data)
