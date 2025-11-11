import requests
from data.endpoints import Endpoints


class BaseAPI:
    def __init__(self):
        self.base_url = Endpoints.BASE_URL

    def post(self, endpoint, json=None, data=None):
        url = f"{self.base_url}{endpoint}"
        return requests.post(url, json=json, data=data)

    def get(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"
        return requests.get(url, params=params)

    def delete(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        return requests.delete(url)