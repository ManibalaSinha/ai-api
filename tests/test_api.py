from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_ask():
    response = client.post("/ask", json={"query": "What is Python?"})
    assert response.status_code == 200
    assert "answer" in response.json()
