import requests
import allure

@allure.feature("API Testing")
@allure.story("GET Request")
@allure.severity(allure.severity_level.NORMAL)
def test_natalie():
    with allure.step("Отправка Get запроса"):
         endpoint = "https://swapi.dev/api/people/5"
         response = requests.get(endpoint)
    with allure.step("Проверка ответа"):
        actual_data = response.json()
        assert response.status_code==200,f"must be 200 but got{response.status_code}"
        assert len(actual_data)>0
        expected_data= {
        "name": "Leia Organa",
        "height": "150",
        "mass": "49",
        "hair_color": "brown",
        "skin_color": "light",
        "eye_color": "brown",
        "birth_year": "19BBY",
        "gender": "female",
        "homeworld": "https://swapi.dev/api/planets/2/",
        "films": [
            "https://swapi.dev/api/films/1/",
            "https://swapi.dev/api/films/2/",
            "https://swapi.dev/api/films/3/",
            "https://swapi.dev/api/films/6/"
        ],
        "species": [],
        "vehicles": [
            "https://swapi.dev/api/vehicles/30/"
        ],
        "starships": [],
        "created": "2014-12-10T15:20:09.791000Z",
        "edited": "2014-12-20T21:17:50.315000Z",
        "url": "https://swapi.dev/api/people/5/"
    }
        assert expected_data==actual_data,"wrong body data"