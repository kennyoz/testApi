
import requests
import json
import pytest

def test_not_found_id():
    url = "https://swapi.dev/api/people/999999999"
    response = requests.get(url)
    actual_data = response.json()
    expected_data = {
    "detail": "Not found"
    }
    assert response.status_code == 404,f"Expected status code 404, but got {response.status_code}"
    assert actual_data ==expected_data,f"Expected body 'detail:Not found'{actual_data}"