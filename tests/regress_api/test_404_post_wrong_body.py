import requests


def test_create_user_with_missing_field():
    url = "https://reqres.in/api/users"

    payload = {
        "name": "A" * 500,  #???????
        "job": "Developer"
    }
    response = requests.post(url, json=payload)

    assert response.status_code == 201, f"Expected status code 400 but got {response.status_code}"
    assert response.headers["Content-Type"] == "application/json; charset=utf-8", "Content-Type is not correct"

    response_data = response.json()
