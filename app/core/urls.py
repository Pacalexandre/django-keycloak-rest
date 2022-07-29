"""Rotas Definidas"""
from rest_framework.routers import DefaultRouter
from .views import ViewProduto, ViewCategoria, ViewNotaFiscal

router = DefaultRouter(trailing_slash=True)

router.register('', ViewProduto, basename='produto')
router.register('', ViewCategoria, basename='categoria')
router.register('', ViewNotaFiscal, basename='nota-fiscal')
