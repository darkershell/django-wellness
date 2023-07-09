import pytest
from django.urls import reverse

@pytest.fixture
def resp(client):
    return client.get(reversed('login'))

def test_login_form_page(resp):
    assert resp.status_code == 200
