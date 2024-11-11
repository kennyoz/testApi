import requests
import json
import pytest

def test_R2_D2():
    url = "https://swapi.dev/api/people/3"
    response = requests.get(url)
    assert response.status_code == 200
    actual_data = response.json()
    with open("C:/Users/kenya/PycharmProjects/testApi/tests/Starwars/Test_id/positive/R2_D2/R2_D2.json", "r") as f:
        expected_data = json.load(f)
    assert actual_data == expected_data, "API response does not match the expected JSON"