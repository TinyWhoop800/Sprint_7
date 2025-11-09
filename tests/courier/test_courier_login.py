import pytest
import allure
from utils.generators import generate_unique_login, generate_unique_password


@allure.feature("Логин курьера")
class TestCourierLogin:
    @allure.title("Успешная авторизация курьера")
    def test_login_courier_success(self, courier_api, registered_courier):
        with allure.step("Логин с корректными данными"):
            login_response = courier_api.login_courier(
                registered_courier["login"],
                registered_courier["password"]
            )

        with allure.step("Проверка успешной авторизации"):
            assert login_response.status_code == 200
            assert "id" in login_response.json()
            assert isinstance(login_response.json()["id"], int)

    @allure.title("Авторизация без обязательного поля: {missing_field}")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_login_missing_required_field(self, courier_api, missing_field):
        with allure.step(f"Генерация данных без поля {missing_field}"):
            login = generate_unique_login() if missing_field != "login" else ""
            password = generate_unique_password() if missing_field != "password" else ""

        with allure.step("Отправка запроса с неполными данными"):
            response = courier_api.login_courier(login, password)

        with allure.step("Проверка ошибки валидации"):
            assert response.status_code == 400
            assert response.json() == {"code": 400, "message": "Недостаточно данных для входа"}

    @allure.title("Авторизация с неправильным логином")
    def test_login_wrong_login(self, courier_api, registered_courier):
        with allure.step("Генерация неправильного логина"):
            wrong_login = generate_unique_login()

        with allure.step("Попытка логина с неправильным логином"):
            response = courier_api.login_courier(wrong_login, registered_courier["password"])

        with allure.step("Проверка ошибки неверных учетных данных"):
            assert response.status_code == 404
            assert response.json() == {"code": 404, "message": "Учетная запись не найдена"}

    @allure.title("Авторизация с неправильным паролем")
    def test_login_wrong_password(self, courier_api, registered_courier):
        with allure.step("Генерация неправильного пароля"):
            wrong_password = generate_unique_password()

        with allure.step("Попытка логина с неправильным паролем"):
            response = courier_api.login_courier(registered_courier["login"], wrong_password)

        with allure.step("Проверка ошибки неверных учетных данных"):
            assert response.status_code == 404
            assert response.json() == {"code": 404, "message": "Учетная запись не найдена"}

    @allure.title("Авторизация несуществующего курьера")
    def test_login_nonexistent_courier(self, courier_api):
        with allure.step("Генерация случайных учетных данных"):
            login = generate_unique_login()
            password = generate_unique_password()

        with allure.step("Попытка логина несуществующего курьера"):
            response = courier_api.login_courier(login, password)

        with allure.step("Проверка ошибки не найденной учетной записи"):
            assert response.status_code == 404
            assert response.json() == {"code": 404, "message": "Учетная запись не найдена"}