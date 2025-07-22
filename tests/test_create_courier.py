import requests
import allure
from data import ResponseBody, DataForRegistration
from curl import Url
import pytest

class TestsCreateCourier:

    @allure.title('Проверка создания нового курьера. Ручка:/api/v1/courier')
    def test_creation_courier_success(self, generate_courier_data):
        with allure.step('Отправка запроса на создание курьера'):
            registration = requests.post(Url.create_courier_url(), json=generate_courier_data[0])
        assert registration.status_code == 201 and (registration.json() == ResponseBody.COURIER_CREATION_SUCCESS)

    @allure.title('Ошибка регистрации двух одинаковых курьеров. Ручка:/api/v1/courier')
    def test_creation_courier_double_error(self, create_courier):
        with allure.step('Первая регистрация курьера'):
            requests.post(Url.create_courier_url(), json=create_courier[0])
        with allure.step('Повторная регистрация того же курьера'):
            response = requests.post(Url.create_courier_url(), json=create_courier[0])
        assert response.status_code == 409 and (response.json() == ResponseBody.COURIER_NAME_ALREADY_EXIST)

    @allure.title('Ошибка: недостаточные данных для регистрации курьера. Нет логина или пароля.')
    @pytest.mark.parametrize('data_setup', DataForRegistration.reg_data)
    def test_creation_courier_deficit_data_error(self, data_setup):
        with allure.step('Отправка запроса с неполными данными'):
            response = requests.post(Url.create_courier_url(), data_setup)
        assert response.status_code == 400 and (response.json() == ResponseBody.COURIER_REGISTRATION_NOT_ENOUGH_DATA)
