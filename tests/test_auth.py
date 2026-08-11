from api.client_api import APIClient
from conftest import authenticated_user

api = APIClient()
#Prueba de login
def test_success_login():
    payload = {
        'username':'emilys',
        'password': 'emilyspass',
        'expiresInMins': 60
    }
    response = api.auth.login(payload)
    data = response.json()

    assert response.status_code == 200
    assert data['username'] == payload['username']
    assert 'accessToken' in data
    assert data['accessToken']
    assert response.elapsed.total_seconds() < 2

#Prueba de logout
def test_success_logout(authenticated_user):
    authenticated_user.auth.logout() #Se llama la fixture con una sesión valida para hacer el logout
    assert 'Authorization' not in authenticated_user.session.headers


def test_failure_login():

    payload = {
        'username':'Arte',
        'password': 'Daniel',
        'expiresInMins': 60
    }
    response = api.auth.login(payload)
    data = response.json()

    assert response.status_code == 400
    assert 'accessToken' not in data
    assert response.elapsed.total_seconds() < 2


def test_current_user(authenticated_user):
    response = api.auth.current_user()

    assert response.status_code == 200



