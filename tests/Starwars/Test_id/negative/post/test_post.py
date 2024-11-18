import requests

def test_post_m():
    url = "https://swapi.dev/api/people/5"
    body_mei={
        "name":"obivan",
        "lastname":"kenobi"
    }
    response = requests.post(url,body_mei)
    assert response.status_code==405
    actual_data = response.json()
    expected ={
            "detail": "Method 'POST' not allowed."
        }
    assert expected == actual_data
