import requests
import json
import allure


def test_create_user():
    with allure.step("Отправка POST запроса"):
        url = "https://reqres.in/api/users"
        payload = {
        "name": "John Doerti",
        "job": "qa engineer"
        }
        response = requests.post(url, json=payload)
    with allure.step("Проверка ответа"):
        assert response.status_code == 201, f"Expected status code 201 but got {response.status_code}"
        response_data = response.json()

        assert "name" in response_data, "Response does not contain 'name'"
        assert "job" in response_data, "Response does not contain 'job'"
        assert response_data["name"] == payload[
        "name"], f"Expected name '{payload['name']}', but got {response_data['name']}"
        assert response_data["job"] == payload["job"], f"Expected job '{payload['job']}', but got {response_data['job']}"
        assert "id" in response_data, "Response does not contain 'id'"
        assert response_data["id"] is not None, "Response id should not be None"
        assert "createdAt" in response_data, "Response does not contain 'createdAt'"
        assert response.elapsed.total_seconds() < 1

