import requests

from utils.config import BASE_URL, DEFAULT_HEADERS
from api.products_api import ProductsAPI
from api.users_api import UsersAPI
from api.auth_api import AuthAPI

class APIClient:
    def __init__(self):
        self.base_url = BASE_URL
        self.session = requests.Session()
        self.session.headers.update(DEFAULT_HEADERS)
        self.users = UsersAPI(self.session, self.base_url)
        self.auth = AuthAPI(self.session, self.base_url)
        self.products = ProductsAPI(self.session, self.base_url)