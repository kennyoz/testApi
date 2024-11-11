import requests
import json
import pytest

def test_ge_by_id():
    url = "https://restful-booker.herokuapp.com/booking/1"
    response = requests.get(url)
    assert response.status_code == 200

