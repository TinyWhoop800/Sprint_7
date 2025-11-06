import allure
from api.base_api import BaseAPI
from data.endpoints import Endpoints


class OrderAPI(BaseAPI):
    @allure.step("Создание заказа")
    def create_order(self, order_data):
        return self.post(Endpoints.ORDER_CREATE, json=order_data)

    @allure.step("Получение списка заказов")
    def get_orders_list(self, params=None):
        return self.get(Endpoints.ORDER_LIST, params=params)