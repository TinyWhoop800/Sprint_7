import allure


@allure.feature("Список заказов")
class TestOrderList:
    @allure.title("Получение списка заказов")
    def test_get_orders_list_returns_list(self, order_api):
        with allure.step("Запрос списка заказов"):
            response = order_api.get_orders_list()

        with allure.step("Проверка успешного ответа"):
            assert response.status_code == 200

        with allure.step("Проверка структуры ответа"):
            response_data = response.json()
            assert "orders" in response_data
            assert isinstance(response_data["orders"], list)