"""Views"""
from rest_framework.views import ModelViewSet
from .models import Produto, Categoria, Notafiscal


class ViewProduto(ModelViewSet):
    queryset = Produto.objects.all()
    


class ViewCategoria(ModelViewSet):
    queryset = Categoria.objects.all()


class ViewNotaFiscal(ModelViewSet):
    queryset = Notafiscal.objects.all()

