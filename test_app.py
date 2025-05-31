import pytest
from app import app
import json

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to the simple Python web server!" in response.data

def test_status(client):
    response = client.get("/status")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "running"
    assert data["message"] == "Everything is OK."

def test_echo_valid_json(client):
    payload = {"key": "value"}
    response = client.post("/echo", json=payload)
    assert response.status_code == 200
    data = response.get_json()
    assert data["you_sent"] == payload

def test_echo_invalid_json(client):
    response = client.post("/echo", data="not-json", content_type="application/json")
    assert response.status_code == 400 or response.status_code == 500  # Flask may return either
