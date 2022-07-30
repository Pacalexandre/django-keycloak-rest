"""Views"""
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin,UpdateModelMixin
from .serializers import CategoriaSerializer, NotaFiscalSerializer, ProdutoCreateSerializer, ProdutoSerializer
from .models import Produto, Categoria, NotaFiscal


class ViewProduto(ListModelMixin, CreateModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = Produto.objects.all()
    def get_serializer_class(self):
        if self.action in ('create','update'):
            return ProdutoCreateSerializer
        if self.action in ('list','retrieve'):
            return ProdutoSerializer


class ViewCategoria(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class ViewNotaFiscal(ModelViewSet):
    queryset = NotaFiscal.objects.all()
    serializer_class = NotaFiscalSerializer
