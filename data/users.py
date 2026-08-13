# Datos de prueba para el módulo de autenticación y usuarios
# Estas credenciales corresponden al usuario de prueba de DummyJSON
VALID_USER = {
    "username": "emilys",
    "password": "emilyspass",
    "expiresInMins": 60,
}

INVALID_USER = {
    "username": "arte",
    "password": "daniel",
    "expiresInMins": 60,
}

CREATE_USER_PAYLOAD = {
    "firstName": "John",
    "lastName": "Doe",
    "email": "john.doe@example.com",
    "username": "johndoe",
    "password": "johndoepass",
}

UPDATE_USER_PAYLOAD = {
    "firstName": "John",
    "lastName": "Smith",
    "email": "john.smith@example.com",
}

PARTIAL_USER_PAYLOAD = {
    "email": "new.john@example.com",
}
