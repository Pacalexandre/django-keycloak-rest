"""Views"""
from rest_framework.viewsets import ModelViewSet
from .serializers import CategoriaSerializer, NotaFiscalSerializer, ProdutoCreateSerializer, ProdutoSerializer
from .models import Produto, Categoria, NotaFiscal


class ViewProduto(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    def get_serializer_class(self):
        if self.action == ('create','update'):
            return ProdutoCreateSerializer


class ViewCategoria(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class ViewNotaFiscal(ModelViewSet):
    queryset = NotaFiscal.objects.all()
    serializer_class = NotaFiscalSerializer
