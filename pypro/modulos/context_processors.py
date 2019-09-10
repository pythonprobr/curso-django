from pypro.modulos import facade


def listar_modulos(request):
    return {'MODULOS': facade.listar_modulos_ordenados()}
