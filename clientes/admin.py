from django.contrib import admin

from clientes.models import Clientes


@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'cpf', 'rg', 'celular', 'ativo')
    list_display_links = ('nome',)
    search_fields = ['nome', 'cpf']
