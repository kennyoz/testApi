import requests
import allure

@allure.feature("API Testing")
@allure.story("GET Request")
@allure.severity(allure.severity_level.NORMAL)
def test_chewbacca():
    with allure.step("Оправка GET запроса"):
         endpoint = "https://swapi.dev/api/people/13"
         response = requests.get(endpoint)
    with allure.step("Сравнение ответа"):
         actual_data = response.json()
         assert response.status_code == 200, f"Must be 200  but got{response.status_code}"
         assert len(actual_data) > 0
         expected_data={
        "name": "Chewbacca",
        "height": "228",
        "mass": "112",
        "hair_color": "brown",
        "skin_color": "unknown",
        "eye_color": "blue",
        "birth_year": "200BBY",
        "gender": "male",
        "homeworld": "https://swapi.dev/api/planets/14/",
        "films": [
            "https://swapi.dev/api/films/1/",
            "https://swapi.dev/api/films/2/",
            "https://swapi.dev/api/films/3/",
            "https://swapi.dev/api/films/6/"
        ],
        "species": [
            "https://swapi.dev/api/species/3/"
        ],
        "vehicles": [
            "https://swapi.dev/api/vehicles/19/"
        ],
        "starships": [
            "https://swapi.dev/api/starships/10/",
            "https://swapi.dev/api/starships/22/"
        ],
        "created": "2014-12-10T16:42:45.066000Z",
        "edited": "2014-12-20T21:17:50.332000Z",
        "url": "https://swapi.dev/api/people/13/"
    }
         assert expected_data==actual_data,"Wrong body"