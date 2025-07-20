import allure
import requests
from data import Flags, OrderData
from curl import Url
import pytest

class TestCreationOrder:

    @allure.title('Проверка создания заказа с выбором разных цветов самоката. Ручка:/api/v1/orders')
    @pytest.mark.parametrize('scooter_color', OrderData.scooter_color)
    def test_create_order_with_colors(self, scooter_color):
        order_data = OrderData.order_data
        order_data['color'] = scooter_color
        order = requests.post(f'{Url.MAIN_URL}{Url.CREATE_ORDER}', json=order_data)
        assert order.status_code == 201 and Flags.SUCCESSFUL_ORDER_CREATION in order.json()
        requests.put(f'{Url.MAIN_URL}{Url.ORDER_CANCEL}{order.json()['track']}')