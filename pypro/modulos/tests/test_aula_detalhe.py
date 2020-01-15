import pytest
from django.urls import reverse
from model_mommy import mommy

from pypro.django_assertions import assert_contains
from pypro.modulos.models import Aula, Modulo


@pytest.fixture
def modulo(db):
    return mommy.make(Modulo)


@pytest.fixture
def aula(modulo):
    return mommy.make(Aula, modulo=modulo)


@pytest.fixture
def resp(client, aula):
    resp = client.get(reverse('modulos:aula', kwargs={'slug': aula.slug}))
    return resp


def test_titulo(resp, aula: Aula):
    assert_contains(resp, aula.titulo)


def test_vimeo(resp, aula: Aula):
    assert_contains(resp, f'src="https://player.vimeo.com/video/{ aula.vimeo_id }"')
