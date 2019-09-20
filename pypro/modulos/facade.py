from typing import List

from pypro.modulos.models import Modulo


def listar_modulos_ordenados() -> List[Modulo]:
    """
    Lista módulos ordenados por parâmetro order
    :return:
    """

    return list(Modulo.objects.order_by('order').all())


def encontrar_modulo(slug: str) -> Modulo:
    return Modulo.objects.get(slug=slug)


def listar_aulas_de_modulo_ordenadas(modulo: Modulo):
    return list(modulo.aula_set.order_by('order').all())
