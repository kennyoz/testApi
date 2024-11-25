import allure
import requests

endpoint = "https://swapi.dev/api/people/5"

@allure.feature("API Testing")
@allure.story("POST Request")
@allure.tag("NEGATIVE")
@allure.severity(allure.severity_level.MINOR)
def test_natalie_portman_post_negative():
   response = requests.post(endpoint)
   assert response.status_code == 4200





@allure.feature("API Testing")
@allure.story("PUT Request")
@allure.tag("NEGATIVE")
@allure.severity(allure.severity_level.MINOR)
def test_natalie_portman_put_negative():
    with allure.step("PUT to endpoint"):
        response = requests.put(endpoint)
    with allure.step("response comparison"):
        data = response.json()
        assert response.status_code == 400,f"must be 405 but got {response.status_code}"
        expected = {
                "detail": "Method 'PUT' not allowed."
        }
        assert data == expected,f"expected body = actual body"

@allure.feature("API Testing")
@allure.story("DELETE Request")
@allure.tag("NEGATIVE")
@allure.severity(allure.severity_level.MINOR)
def test_natalie_portman_delete_negative():
    with allure.step("DELETE to endpoint"):
        response = requests.delete(endpoint)
    with allure.step("response comparison"):
        data = response.json()
        assert response.status_code == 405,f"must be 405 but got {response.status_code}"
        expected = {
                "detail": "Method 'DELETE' not allowed."
        }
        assert data == expected,f"expected body = actual body"