import requests
import allure



@allure.feature("API Testing")
@allure.story("GET Request")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_search():
    with allure.step("Отправка GET-запроса"):
         endpoint = "https://brands4pets.ru/data/catalog/products/?search=%D0%BA%D1%83%D0%BA%D1%83"
         response = requests.get(endpoint)

    with allure.step("Проверка ответа"):
         cook = response.json()
         assert response.status_code==200


