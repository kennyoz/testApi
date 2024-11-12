import requests


def test_get_users():
    url = "https://reqres.in/api/users"
    response = requests.get(url)

    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
    response_data = response.json()
    assert "data" in response_data, "Response JSON does not contain 'data' key"
    assert len(response_data["data"]) > 0, "User list is empty"

    first_user = response_data["data"][0]
    assert "id" in first_user, "does not have 'id'"
    assert "email" in first_user, "does not have 'email'"
    assert "first_name" in first_user, "does not have 'first_name'"
    assert "last_name" in first_user, "does not have 'last_name'"

    assert first_user["id"] == 1, f"Expected id 1, but got {first_user['id']}"
    assert first_user[
               "email"] == "george.bluth@reqres.in", f"Expected email george.bluth@reqres.in, but got {first_user['email']}"
    