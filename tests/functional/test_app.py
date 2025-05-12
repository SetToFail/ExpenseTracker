import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['DATABASE'] = ':memory:'
    
    with app.test_client() as client:
        with app.app_context():
            yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert isinstance(response.json, dict)  # Проверяем что возвращается словарь
    assert 'expenses' in response.json  # Проверяем наличие ключа