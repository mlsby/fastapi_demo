from fastapi.testclient import TestClient
from main import app


def test_read_main():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Toxicity classifyer"}

def test_predict():
    with TestClient(app) as client:
        nice_response = client.post(
            "/predict",
            json={"input_text": "I love you"}
        )
        toxic_response = client.post(
            "/predict",
            json={"input_text": "I hate your guts"}
        )
        assert not nice_response.json()['toxic']
        assert toxic_response.json()['toxic']
