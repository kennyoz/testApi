import requests
from getpass import getpass


def test_api_lol():
    response = requests.get('https://api.github.com')
    print(response.headers)
    print(response.text)
    print(response.content)


def test_api_login():
    response = requests.get('https://api.github.com/user', auth=('kennyoz', "437173471"))
    assert response.status_code == 401
    print(response.headers)
    print(response.json())