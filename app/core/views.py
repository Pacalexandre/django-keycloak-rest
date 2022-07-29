"""Views"""
from rest_framework.viewsets import ModelViewSet

from .serializers import CategoriaSerializer, NotaFiscalSerializer, ProdutoSerializer
from .models import Produto, Categoria, NotaFiscal


class ViewProduto(ModelViewSet):
    queryset = Produto.objects.all()
    serializer = ProdutoSerializer


class ViewCategoria(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer = CategoriaSerializer


class ViewNotaFiscal(ModelViewSet):
    queryset = NotaFiscal.objects.all()
    serializer = NotaFiscalSerializer
