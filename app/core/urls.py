"""Rotas Definidas"""
from rest_framework.routers import DefaultRouter
from .views import ViewProduto, ViewCategoria, ViewNotaFiscal

router = DefaultRouter(trailing_slash=False)

router.register('v1/produto', ViewProduto, basename='produto')
router.register('v1/categoria', ViewCategoria, basename='categoria')
router.register('v1/nota-fiscal', ViewNotaFiscal, basename='nota-fiscal')
