class BaseAPI:

    def __init__(self, session,base_url):
        self.base_url = base_url
        self.session = session

    def _request(self, method, endpoint, payload=None, params=None): #Metodo interno para reutilizar código ye vitar duplicación
        return self.session.request(
            method,
            self.base_url + endpoint,
            json=payload,
            params=params,
        )

    def get(self, endpoint, params=None):
       return self._request("get", endpoint, params=params)

    def post(self, endpoint, payload=None):
        return self._request("post", endpoint, payload)

    def delete(self, endpoint):
        return self._request("delete", endpoint)

    def put(self, endpoint, payload=None):
        return self._request("put", endpoint, payload)

    def patch(self, endpoint,payload=None, params=None):
        return self._request("patch", endpoint,payload=payload, params=params,)








