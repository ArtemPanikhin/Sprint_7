import allure
import requests
from data import Flags, OrderData
from curl import Url
import pytest

class TestCreationOrder:

    @allure.title('Проверка создания заказа с выбором разных цветов самоката. Ручка:/api/v1/orders')
    @pytest.mark.parametrize('scooter_color', OrderData.scooter_color)
    def test_create_order_with_colors(self, cancel_order, scooter_color):
        with allure.step('Подготовка данных заказа с цветом: ' + str(scooter_color)):
            order_data = OrderData.order_data.copy()
            order_data['color'] = scooter_color
        with allure.step('Отправка запроса на создание заказа'):
            order = requests.post(Url.create_order_url(), json=order_data)
        with allure.step('Получение номера трека заказа'):
            track = order.json()['track']
        with allure.step('Регистрация заказа для отмены после теста'):
            cancel_order.append(track)
        assert order.status_code == 201 and Flags.SUCCESSFUL_ORDER_CREATION in order.json()