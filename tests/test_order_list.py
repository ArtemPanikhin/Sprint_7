import allure
import requests
from data import Flags
from curl import Url


class TestGetOrderList:

    @allure.title('Проверка получения списка заказов. Ручка:/api/v1/orders')
    def test_successful_get_order_list(self):
        with allure.step('Отправка запроса на получение списка заказов'):
            response = requests.get(Url.get_order_list_url())
        assert response.status_code == 200 and Flags.SUCCESSFUL_GET_ORDER_LIST in response.json()