from api.base_api import BaseAPI

class AuthAPI(BaseAPI):#Esta API se encargará de hacer el proceso de autenticación y almacenar/refrescar el JWT en los headers de la sesión

    def _set_token(self, token): #Metodo interno para actualizar el JWT en los headers de la sesión.
        self.session.headers.update({
            'Authorization': f"Bearer {token}"
        })

    def login(self, payload): #Metodo para hacer login
        response = self.post('/auth/login', payload)

        if response.status_code == 200: #Condición que activará el metodo interno
            self._set_token(response.json()['accessToken']) #Convierte el response a JSON y extraer el accesstoken para actualizarlo en el metodo interno.

        return response

    def current_user(self): #Metodo para traer el usuario con la sesión activa actual.
        return self.get('/auth/me')

    def refresh_token(self): #Metodo para refrescar la sesión
        response = self.get('/auth/refresh')
        if response.status_code == 200: #Condición que activará el metodo interno
            self._set_token(response.json()['accessToken']) #Convierte el response a JSON y extraer el accesstoken para actualizarlo en el metodo interno.

        return response

    def logout(self): #Metodo para cerrar sesión
        self.session.headers.pop('Authorization', None) #Elimina el accessToken de los headers de la sesión actual.