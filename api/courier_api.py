import allure
from api.base_api import BaseAPI
from data.endpoints import Endpoints


class CourierAPI(BaseAPI):
    @allure.step("Создание курьера с логином {login}")
    def create_courier(self, login, password, first_name):
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        return self.post(Endpoints.COURIER_CREATE, data=payload)

    @allure.step("Логин курьера с логином {login}")
    def login_courier(self, login, password):
        payload = {
            "login": login,
            "password": password
        }
        return self.post(Endpoints.COURIER_LOGIN, data=payload)

    @allure.step("Удаление курьера с ID {courier_id}")
    def delete_courier(self, courier_id):
        return self.delete(Endpoints.COURIER_DELETE.format(id=courier_id))