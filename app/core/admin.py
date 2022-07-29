from django.contrib import admin
from .models import Categoria, NotaFiscal, Produto


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nome', 'categoria', 'preco']
    ordering = ['codigo']


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    ordering = ['id']


class NotaFiscalAdmin(admin.ModelAdmin):
    list_display = ['id', 'numero', 'produto', 'qnt']


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(NotaFiscal, NotaFiscalAdmin)
