from api.client_api import APIClient

api = APIClient()

#Prueba de humo
def test_get_all_products():

    response = api.products.get_all_products()

    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 2

#Prueba de estructura de contrato
def test_get_product_structure():
    response = api.products.get_all_products()

    assert response.status_code == 200

    data = response.json()
    product = data['products'][0]

    assert "products" in data
    assert "total" in data
    assert "skip" in data
    assert "limit" in data

    assert isinstance(data["products"], list)
    assert isinstance(data["total"], int)
    assert isinstance(data["skip"], int)
    assert isinstance(data["limit"], int)

    assert "id" in product
    assert "title" in product
    assert "description" in product
    assert "price" in product
    assert "category" in product

    assert isinstance(product["id"], int)
    assert isinstance(product["title"], str)
    assert isinstance(product["description"], str)
    assert isinstance(product["price"], (int, float))
    assert isinstance(product["category"], str)

#Prueba de consistencia del recurso solicitado
def test_get_product_by_id():
    product_id = 5
    response = api.products.get_product_by_id(product_id)

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == product_id
    assert isinstance(data["id"], int)
    assert "title" in data
    assert "price" in data
    assert "category" in data