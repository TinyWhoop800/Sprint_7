import pytest
import allure
from api.courier_api import CourierAPI
from utils.generators import generate_unique_login, generate_unique_password, generate_unique_first_name
from api.order_api import OrderAPI


@pytest.fixture
def courier_api():
    return CourierAPI()

@pytest.fixture
def order_api():
    return OrderAPI()

@pytest.fixture
def cleanup_courier(courier_api):
    couriers_to_delete = []
    yield couriers_to_delete
    with allure.step("Очистка созданных курьеров"):
        for login, password in couriers_to_delete:
            login_response = courier_api.login_courier(login, password)
            if login_response.status_code == 200:
                courier_id = login_response.json()["id"]
                courier_api.delete_courier(courier_id)

@pytest.fixture
def registered_courier(courier_api, cleanup_courier):
    login = generate_unique_login()
    password = generate_unique_password()
    first_name = generate_unique_first_name()
    create_response = courier_api.create_courier(login, password, first_name)
    assert create_response.status_code == 201
    cleanup_courier.append((login, password))
    return {
        "login": login,
        "password": password,
        "first_name": first_name
    }