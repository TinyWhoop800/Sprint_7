import pytest
import allure
from data.test_data import TestData


@allure.feature("Создание заказа")
class TestOrderCreation:
    @allure.title("Создание заказа с цветами: {color}")
    @pytest.mark.parametrize("color", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        None,
        []
    ])
    def test_create_order_with_different_colors(self, order_api, color):
        with allure.step("Подготовка данных заказа"):
            order_data = TestData.get_order_data(color=color)

        with allure.step("Отправка запроса на создание заказа"):
            response = order_api.create_order(order_data)

        with allure.step("Проверка успешного создания"):
            assert response.status_code == 201

        with allure.step("Проверка наличия track номера"):
            response_data = response.json()
            assert "track" in response_data
            assert isinstance(response_data["track"], int)

    @allure.title("Создание заказа с обязательными полями")
    def test_create_order_required_fields(self, order_api):
        with allure.step("Подготовка данных только с обязательными полями"):
            order_data = TestData.get_order_data(color=None)

        with allure.step("Отправка запроса на создание заказа"):
            response = order_api.create_order(order_data)

        with allure.step("Проверка успешного создания"):
            assert response.status_code == 201
            assert "track" in response.json()