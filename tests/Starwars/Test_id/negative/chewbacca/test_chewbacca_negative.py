import requests
import allure
endpoint = "https://swapi.dev/api/people/13"


@allure.feature("API Testing")
@allure.story("POST Request")
@allure.tag("NEGATIVE")
@allure.severity(allure.severity_level.MINOR)
def test_chewbacca_post_negative():
    with allure.step("Post to endpoint"):
        response = requests.post(endpoint)
    with allure.step("response comparison"):
        expected = {
                "detail": "Method 'POST' not allowed."
        }
        assert response.status_code == 405,f"must be 405 but got {response.status_code}"
        data = response.json()
        assert expected == data ,f"expected body = actual body"


@allure.feature("API Testing")
@allure.story("PUT Request")
@allure.tag("NEGATIVE")
@allure.severity(allure.severity_level.MINOR)
def test_chewbacca_put_negative():
    with allure.step("PUT to endpoint"):
        response = requests.put(endpoint)
    with allure.step("response comparison"):
        assert response.status_code == 405,f"must be 405 but got {response.status_code}"
        expected_data = {
    "detail": "Method 'PUT' not allowed."
    }
        data = response.json()
        assert data == expected_data,f"expected body = actual body"


@allure.feature("API Testing")
@allure.story("DELETE Request")
@allure.tag("NEGATIVE")
@allure.severity(allure.severity_level.MINOR)
def test_chewbacca_delete_negative():
    with allure.step("DELETE to endpoint"):
        response = requests.delete(endpoint)
    with allure.step("response comparison"):
        assert response.status_code == 405,f"must be 405 but got {response.status_code}"
        expected_data = {
    "detail": "Method 'DELETE' not allowed."
    }
        data = response.json()
        assert data == expected_data,f"expected body = actual body"