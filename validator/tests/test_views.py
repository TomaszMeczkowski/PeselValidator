import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_home_get(client):
    url = reverse("home")
    response = client.get(url)
    assert response.status_code == 200
    # assert b"Walidator PESEL" in response.content


@pytest.mark.django_db
def test_home_post_valid(client):
    url = reverse("home")
    response = client.post(url, {"pesel": "44051401359"})
    assert response.status_code == 200
    print(response.content)
    # assert b"PESEL Poprawny" in response.content


@pytest.mark.django_db
def test_home_post_invalid(client):
    url = reverse("home")
    response = client.post(url, {"pesel": "12345678901"})
    assert response.status_code == 200
    # assert b"PESEL Niepoprawny" in response.content
