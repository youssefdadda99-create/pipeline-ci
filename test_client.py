from main import app
from fastapi.testclient import TestClient


client = TestClient(app)


def test_data():
    response = client.get("/data")
    assert response.status_code == 200
    assert len(response.json()) > 0



