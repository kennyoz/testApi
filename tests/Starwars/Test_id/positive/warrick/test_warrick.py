import requests
import allure

@allure.feature("API Testing")
@allure.story("GET Request")
@allure.severity(allure.severity_level.NORMAL)
def test_warick():
    endpoint = "https://swapi.dev/api/people/30"
    response = requests.get(endpoint)
    actual_data = response.json()
    assert response.status_code==200
    assert len(actual_data)>0
    expected_data = {
	"name": "Wicket Systri Warrick",
	"height": "88",
	"mass": "20",
	"hair_color": "brown",
	"skin_color": "brown",
	"eye_color": "brown",
	"birth_year": "8BBY",
	"gender": "male",
	"homeworld": "https://swapi.dev/api/planets/7/",
	"films": [
		"https://swapi.dev/api/films/3/"
	],
	"species": [
		"https://swapi.dev/api/species/9/"
	],
	"vehicles": [],
	"starships": [],
	"created": "2014-12-18T11:21:58.954000Z",
	"edited": "2014-12-20T21:17:50.369000Z",
	"url": "https://swapi.dev/api/people/30/"
}
    assert expected_data==actual_data
