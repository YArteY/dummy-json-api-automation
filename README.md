# Dummy JSON API Automation

Framework automatizado y reutilizable para pruebas de API construido con **Python + pytest + requests**. Está enfocado en la API pública de [DummyJSON](https://dummyjson.com), pero está diseñado para adaptarse fácilmente a cualquier API REST.

## Características

- Sesión HTTP reutilizable con autenticación JWT automática.
- Capa de API por recurso (`auth`, `products`, `users`) con wrappers tipados por endpoint.
- Datos de prueba centralizados en `data/`.
- Validadores reutilizables para contratos de respuesta.
- Reporte HTML automático con `pytest-html`.
- Configuración por variables de entorno.

## Requisitos

- Python 3.9+
- pip

## Instalación

```bash
# 1. Crear y activar el entorno virtual
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # Linux/macOS

# 2. Instalar dependencias
pip install -r requirements.txt
```

## Uso

### Ejecutar todas las pruebas

```bash
pytest
```

### Ejecutar un módulo específico

```bash
pytest tests/test_products.py
```

### Ejecutar una prueba específica

```bash
pytest tests/test_auth.py::test_success_login
```

### Ejecutar pruebas de un marcador

```bash
pytest -m smoke
```

Marcadores disponibles: `smoke`, `auth`, `products`, `users`.

### Reporte HTML

Al finalizar cada ejecución se genera `reports/report.html`. Ábrelo en el navegador para ver el detalle de resultados.

## Estructura del proyecto

```
├── api/                     # Capa de cliente HTTP y wrappers por recurso
│   ├── base_api.py          # Métodos HTTP genéricos (get/post/put/patch/delete)
│   ├── client_api.py        # Ensambla la sesión y expone los recursos
│   ├── auth_api.py          # Login/logout/current_user y manejo del JWT
│   ├── products_api.py      # Endpoints de /products
│   └── users_api.py         # Endpoints de /users
├── data/                    # Datos de prueba (payloads, credenciales)
├── tests/                   # Casos de prueba por módulo
├── utils/
│   ├── config.py            # Configuración (URL base, headers, tiempos)
│   └── validators.py        # Validaciones de contrato reutilizables
├── reports/                 # Reportes HTML generados
├── conftest.py              # Fixtures compartidas
└── requirements.txt
```

## Configuración

Puedes sobrescribir la configuración por defecto con variables de entorno:

| Variable | Descripción | Valor por defecto |
|---|---|---|
| `BASE_URL` | URL base de la API | `https://dummyjson.com` |
| `MAX_RESPONSE_TIME_SECONDS` | Tiempo máximo de respuesta aceptado | `2.0` |

## Cómo agregar un nuevo recurso

Ejemplo para agregar el recurso `cart` (carritos):

1. **Crear el wrapper en `api/cart_api.py`** heredando de `BaseAPI`:

   ```python
   from api.base_api import BaseAPI

   class CartAPI(BaseAPI):
       def get_all_carts(self, params=None):
           return self.get('/carts', params=params)

       def get_cart_by_id(self, cart_id):
           return self.get(f'/carts/{cart_id}')
   ```

2. **Registrarlo en `api/client_api.py`**:

   ```python
   self.carts = CartAPI(self.session, self.base_url)
   ```

3. **Crear los datos de prueba en `data/carts.py`**.

4. **Crear `tests/test_carts.py`** usando las fixtures `api_client` y `authenticated_user`:

   ```python
   def test_get_all_carts(api_client):
       response = api_client.carts.get_all_carts()
       assert response.status_code == 200
   ```

5. **Agregar un marcador** en `pytest.ini` si deseas filtrar por módulo.

## Notas

- Las credenciales en `data/users.py` pertenecen al usuario de demostración de DummyJSON.
- En entornos reales, mueve las credenciales a variables de entorno o a un secret manager.
