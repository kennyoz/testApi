
import allure
import requests
@allure.feature("API Testing")
@allure.story("GET Request")
@allure.severity(allure.severity_level.NORMAL)
def test_random():
    endpoint = "https://swapi.dev/api/people/20"
    response = requests.get(endpoint)
    assert response.status_code == 200
    actual_data = response.json()

    assert len(actual_data)>0
