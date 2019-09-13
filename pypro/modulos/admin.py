from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin

from pypro.modulos.models import Modulo


@admin.register(Modulo)
class ModuloAdmin(OrderedModelAdmin):
    list_display = ('titulo', 'publico', 'move_up_down_links')
    prepopulated_fields = {'slug': ('titulo',)}
