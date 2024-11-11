import requests
import json
import pytest
def test_luke_skywalker():
    url = "https://swapi.dev/api/people/1/"
    response = requests.post(url)
    assert response.status_code == 405, f"Expected status code 405, but got {response.status_code}"
    actual_data = response.json()
    expected_data = {
    "detail": "Method 'POST' not allowed."
    }
    assert actual_data == expected_data, "API response does not match the expected JSON"
