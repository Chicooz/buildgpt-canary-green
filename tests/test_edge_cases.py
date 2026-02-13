import requests


def test_empty_input_returns_400():
    response = requests.post('http://localhost:8000/your-endpoint', json={})
    assert response.status_code == 400
