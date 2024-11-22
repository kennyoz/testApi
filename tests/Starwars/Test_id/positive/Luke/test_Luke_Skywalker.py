import requests
import allure

@allure.feature("API Testing")
@allure.story("GET Request")
@allure.severity(allure.severity_level.NORMAL)
def test_luke_skywalker():
    with allure.step("Отправка GET запроса"):
        url = "https://swapi.dev/api/people/1/"
        response = requests.get(url)
    with allure.step("Проверка ответа"):
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
        actual_data = response.json()



        expected_data = {
    "name": "Luke Skywalker",
    "height": "172",
    "mass": "77",
    "hair_color": "blond",
    "skin_color": "fair",
    "eye_color": "blue",
    "birth_year": "19BBY",
    "gender": "male",
    "homeworld": "https://swapi.dev/api/planets/1/",
    "films": [
        "https://swapi.dev/api/films/1/",
        "https://swapi.dev/api/films/2/",
        "https://swapi.dev/api/films/3/",
        "https://swapi.dev/api/films/6/"
    ],
    "species": [],
    "vehicles": [
        "https://swapi.dev/api/vehicles/14/",
        "https://swapi.dev/api/vehicles/30/"
    ],
    "starships": [
        "https://swapi.dev/api/starships/12/",
        "https://swapi.dev/api/starships/22/"
    ],
    "created": "2014-12-09T13:50:51.644000Z",
    "edited": "2014-12-20T21:17:56.891000Z",
    "url": "https://swapi.dev/api/people/1/"
}
        assert actual_data == expected_data, "API response does not match the expected JSON"

