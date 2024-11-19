

import requests

def test_random():
    endpoint = "https://swapi.dev/api/people/20"
    response = requests.get(endpoint)
    assert response.status_code == 200
    actual_data = response.json()

    assert len(actual_data)<0
