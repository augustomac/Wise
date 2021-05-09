from django.contrib import admin
from estoque.models import Item

class Itens(admin.ModelAdmin):
    list_display = ('id','nome', 'quantidade', 'valor')
    list_display_links = ('id', 'nome', 'quantidade', 'valor')
    search_fields = ('nome',)

admin.site.register(Item, Itens)
