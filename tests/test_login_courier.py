import allure
import requests
from curl import Url
import pytest
import generators
from data import ResponseBody, DataForAutorization


class TestLoginCourier:

    @allure.title('Проверка авторизации курьера. Ручка:/api/v1/courier/login')
    def test_login_courier_success(self, create_courier):
        with allure.step('Отправка запроса на авторизацию курьера'):
            response = requests.post(Url.courier_login_url(), json=create_courier[1])
        assert response.status_code == 200 and response.json().get('id')

    @allure.title('Проверка авторизации несуществующего пользователя. Ручка:/api/v1/courier/login')
    def test_login_courier_unregister(self):
        with allure.step('Генерация тестовых данных для несуществующего пользователя'):
            login_data = {'login': generators.login_generator(), 'password': generators.password_generator()}
        with allure.step('Отправка запроса на авторизацию'):
            response = requests.post(Url.courier_login_url(), login_data)
        assert response.status_code == 404 and (response.json() == ResponseBody.COURIER_ACCOUNT_NOT_FOUND)

    @allure.title('Ошибка: недостаточные данных для авторизации курьера. Нет логина или пароля.')
    @pytest.mark.parametrize('data_setup', DataForAutorization.aut_data)
    def test_creation_courier_deficit_data_error(self, data_setup):
        with allure.step('Отправка запроса с неполными данными'):
            response = requests.post(Url.courier_login_url(), data_setup)
        assert response.status_code == 400 and (response.json() == ResponseBody.COURIER_LOGIN_NOT_ENOUGH_DATA)