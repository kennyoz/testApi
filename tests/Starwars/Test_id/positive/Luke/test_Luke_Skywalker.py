import requests
import json
import pytest


def test_luke_skywalker():
    url = "https://swapi.dev/api/people/1/"

    response = requests.get(url)

    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    actual_data = response.json()

    with open("C:/Users/kenya/PycharmProjects/testApi/tests/Starwars/Test_id/positive/Luke/Get_First_person.json", "r") as f:
        expected_data = json.load(f)

    assert actual_data == expected_data, "API response does not match the expected JSON"

