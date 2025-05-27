from fastapi.testclient import TestClient
from api_main import app

client = TestClient(app)

def test_state():
    response = client.get('/state')
    assert response.status_code == 200
    assert response.json() == {'status': 'Updatopia engine online'}