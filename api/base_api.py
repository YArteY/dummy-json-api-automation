import requests
class BaseAPI:

    def __init__(self):
        self.base_url = 'https://dummyjson.com/'
        self.headers = {
            "Content-Type": "application/json"
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)

    def _request(self, method, endpoint, payload=None, params=None):
        return self.session.request(
            method,
            self.base_url + endpoint,
            json=payload,
            params=params,
        )

    def get(self, endpoint):
       return self._request("get", endpoint)

    def post(self, endpoint, payload=None):
        return self._request("post", endpoint, payload)

    def delete(self, endpoint):
        return self._request("delete", endpoint)

    def put(self, endpoint, payload=None):
        return self._request("put", endpoint, payload)

    def patch(self, endpoint, payload=None):
        return self._request("patch", endpoint, payload)








