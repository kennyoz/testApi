import allure
import requests

endpoint = "https://swapi.dev/api/people/3"

@allure.feature("API Testing")
@allure.story("POST Request")
@allure.tag("NEGATIVE")
@allure.severity(allure.severity_level.MINOR)
def test_R2_D2_post_negative():
    with allure.step("POST_to_url"):
         response = requests.post(endpoint)
         response.status_code==405,f"must be 405 but got{response.status_code}"
    with allure.step("response comparison"):
        data = response.json()
        assert response.status_code == 405,f"must be 405 but got {response.status_code}"
        expected = {
                "detail": "Method 'POST' not allowed."
        }
        assert data == expected,f"expected body = actual body"




@allure.feature("API Testing")
@allure.story("PUT Request")
@allure.tag("NEGATIVE")
@allure.severity(allure.severity_level.MINOR)
def test_R2_D2_put_negative():
    with allure.step("POST_to_url"):
         response = requests.put(endpoint)
         response.status_code==405,f"must be 405 but got{response.status_code}"
    with allure.step("response comparison"):
        data = response.json()
        assert response.status_code == 405,f"must be 405 but got {response.status_code}"
        expected = {
                "detail": "Method 'PUT' not allowed."
        }
        assert data == expected,f"expected body = actual body"


@allure.feature("API Testing")
@allure.story("DELETE Request")
@allure.tag("NEGATIVE")
@allure.severity(allure.severity_level.MINOR)
def test_R2_D2_delete_negative():
    with allure.step("POST_to_url"):
         response = requests.delete(endpoint)
         response.status_code==405,f"must be 405 but got{response.status_code}"
    with allure.step("response comparison"):
        data = response.json()
        assert response.status_code == 405,f"must be 405 but got {response.status_code}"
        expected = {
                "detail": "Method 'DELETE' not allowed."
        }
        assert data == expected,f"expected body = actual body"