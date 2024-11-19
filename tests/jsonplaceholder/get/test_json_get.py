import requests
import pytest


def test_jsonplaysholder_get():
    url = "https://jsonplaceholder.typicode.com/todos/1"
    response = requests.get(url)
    actual = response.json()
    assert len(actual)>0,"response is empty"
    expected={
    "userId": 1,
    "id": 1,
    "title": "delectus aut autem",
    "completed": False
}
    assert response.status_code == 200," Invalid status code"
    assert actual == expected,"The response body is incorrect"