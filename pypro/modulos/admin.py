from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin

from pypro.modulos.models import Aula, Modulo


@admin.register(Modulo)
class ModuloAdmin(OrderedModelAdmin):
    list_display = ('titulo', 'publico', 'move_up_down_links')
    prepopulated_fields = {'slug': ('titulo',)}


@admin.register(Aula)
class AulaAdmin(OrderedModelAdmin):
    list_display = ('titulo', 'modulo', 'order', 'move_up_down_links')
    list_filter = ('modulo',)
    ordering = ('modulo', 'order')
    prepopulated_fields = {'slug': ('titulo',)}
