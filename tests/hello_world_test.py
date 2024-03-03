import pytest
from app import app as flask_app
from flask import json

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_hello(client):
    res = client.get('/')
    assert res.status_code == 200

def test_health(client):
    res=client.get('/health')
    assert res.status_code == 200