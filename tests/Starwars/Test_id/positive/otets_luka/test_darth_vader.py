from http.client import responses


import requests


def test_get_darth_vader():
    url = "https://swapi.dev/api/people/4"
    response = requests.get(url)
    assert response.status_code == 200,f"Status code must be 200 but got{response.status_code}"
    actual_data = response.json()
    assert len(actual_data)>0


    expected = {
    "name": "Darth Vader",
    "height": "202",
    "mass": "136",
    "hair_color": "none",
    "skin_color": "white",
    "eye_color": "yellow",
    "birth_year": "41.9BBY",
    "gender": "male",
    "homeworld": "https://swapi.dev/api/planets/1/",
    "films": [
        "https://swapi.dev/api/films/1/",
        "https://swapi.dev/api/films/2/",
        "https://swapi.dev/api/films/3/",
        "https://swapi.dev/api/films/6/"
    ],
    "species": [],
    "vehicles": [],
    "starships": [
        "https://swapi.dev/api/starships/13/"
    ],
    "created": "2014-12-10T15:18:20.704000Z",
    "edited": "2014-12-20T21:17:50.313000Z",
    "url": "https://swapi.dev/api/people/4/"
}
    assert actual_data == expected ,f"wrong body"