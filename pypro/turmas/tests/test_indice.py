import pytest
from django.urls import reverse


@pytest.fixture
def resp(client, db):
    return client.get(reverse('turmas:indice'))


def test_status_code(resp):
    assert resp.status_code == 200
