import pytest
import allure
from utils.generators import generate_unique_login, generate_unique_password, generate_unique_first_name


@allure.feature("Создание курьера")
class TestCourierCreation:
    @allure.title("Успешное создание курьера")
    def test_create_courier_success(self, courier_api, cleanup_courier):
        with allure.step("Генерация тестовых данных"):
            login = generate_unique_login()
            password = generate_unique_password()
            first_name = generate_unique_first_name()

        with allure.step("Создание курьера через API"):
            response = courier_api.create_courier(login, password, first_name)
            cleanup_courier.append((login, password))

        with allure.step("Проверка успешного ответа"):
            assert response.status_code == 201
            assert response.json() == {"ok": True}

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_duplicate_courier_fails(self, courier_api, cleanup_courier):
        with allure.step("Генерация тестовых данных"):
            login = generate_unique_login()
            password = generate_unique_password()
            first_name = generate_unique_first_name()

        with allure.step("Первое создание курьера"):
            response1 = courier_api.create_courier(login, password, first_name)
            assert response1.status_code == 201
            cleanup_courier.append((login, password))

        with allure.step("Попытка второго создания с теми же данными"):
            response2 = courier_api.create_courier(login, password, first_name)

        with allure.step("Проверка ошибки дублирования"):
            assert response2.status_code == 409
            assert response2.json() == {"code": 409, "message": "Этот логин уже используется. Попробуйте другой."}

    @allure.title("Создание курьера без обязательного поля: {missing_field}")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_create_courier_missing_required_field(self, courier_api, missing_field, cleanup_courier):
        with allure.step(f"Генерация данных без поля {missing_field}"):
            login = generate_unique_login() if missing_field != "login" else None
            password = generate_unique_password() if missing_field != "password" else None
            first_name = generate_unique_first_name()

        with allure.step("Отправка запроса с неполными данными"):
            response = courier_api.create_courier(login, password, first_name)

        with allure.step("Проверка ошибки валидации"):
            assert response.status_code == 400
            assert response.json() == {"code": 400, "message": "Недостаточно данных для создания учетной записи"}

    @allure.title("Создание курьера с уже существующим логином")
    def test_create_courier_existing_login(self, courier_api, cleanup_courier):
        with allure.step("Создание первого курьера"):
            login = generate_unique_login()
            password1 = generate_unique_password()
            first_name1 = generate_unique_first_name()
            response1 = courier_api.create_courier(login, password1, first_name1)
            assert response1.status_code == 201
            cleanup_courier.append((login, password1))

        with allure.step("Попытка создания второго курьера с тем же логином"):
            password2 = generate_unique_password()
            first_name2 = generate_unique_first_name()
            response2 = courier_api.create_courier(login, password2, first_name2)

        with allure.step("Проверка ошибки существующего логина"):
            assert response2.status_code == 409
            assert response2.json() == {"code": 409, "message": "Этот логин уже используется. Попробуйте другой."}