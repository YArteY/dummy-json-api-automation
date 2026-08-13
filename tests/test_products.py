from utils.validators import (
    assert_category_structure,
    assert_product_list_structure,
    assert_product_structure,
    assert_response_time,
)


# Prueba de humo
def test_get_all_products(api_client):
    response = api_client.products.get_all_products()

    assert response.status_code == 200
    assert_response_time(response)


# Prueba de estructura de contrato
def test_get_product_structure(api_client):
    response = api_client.products.get_all_products()

    assert response.status_code == 200
    assert_response_time(response)

    assert_product_list_structure(response.json())


# Prueba de consistencia del recurso solicitado
def test_sucess_get_product_by_id(api_client):
    product_id = 5
    response = api_client.products.get_product_by_id(product_id)

    assert response.status_code == 200
    assert_response_time(response)

    data = response.json()

    assert data["id"] == product_id
    assert_product_structure(data)


def test_failed_get_product_by_id(api_client):
    product_id = 45489
    response = api_client.products.get_product_by_id(product_id)

    assert response.status_code == 404
    assert_response_time(response)


def test_sucess_search_products(api_client):
    response = api_client.products.search_products(query="samsung")

    assert response.status_code == 200
    assert_response_time(response)

    assert_product_list_structure(response.json())


def test_failed_search_products(api_client):
    response = api_client.products.search_products(query="GTA VI")

    assert response.status_code == 200
    assert_response_time(response)

    data = response.json()

    assert "products" in data
    assert data["total"] == 0
    assert data["skip"] == 0
    assert data["limit"] == 0


def test_get_all_categories(api_client):
    response = api_client.products.get_all_categories()

    assert response.status_code == 200
    assert_response_time(response)

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0
    assert_category_structure(data[0])


def test_get_success_products_by_category(api_client):
    response = api_client.products.get_products_by_category(category="smartphones")

    assert response.status_code == 200
    assert_response_time(response)

    assert_product_list_structure(response.json())


def test_failed_get_products_by_category(api_client):
    response = api_client.products.get_products_by_category(category="")

    assert response.status_code == 404
    assert_response_time(response)


def test_success_add_product(api_client):
    payload = {
        "title": "iPhone 16",
        "description": "the perfect balance of price and quality",
        "price": 800,
        "category": "smartphones",
    }
    response = api_client.products.add_product(payload)

    assert response.status_code == 201
    assert_response_time(response)

    assert_product_structure(response.json())


def test_update_product(api_client):
    product_id = 5
    payload = {
        "title": "iPhone 16",
        "description": "the perfect balance of price and quality",
        "price": 800,
        "category": "smartphones",
    }
    response = api_client.products.update_product(product_id, payload)

    assert response.status_code == 200
    assert_response_time(response)

    data = response.json()

    assert data["id"] == product_id
    assert data["title"] == payload["title"]
    assert data["description"] == payload["description"]
    assert data["price"] == payload["price"]
    assert data["category"] == payload["category"]
    assert_product_structure(data)


def test_patch_product(api_client):
    product_id = 5
    payload = {
        "title": "iPhone 16",
    }
    response = api_client.products.patch_product(product_id, payload)

    assert response.status_code == 200
    assert_response_time(response)

    data = response.json()

    assert data["id"] == product_id
    assert data["title"] == payload["title"]
    assert_product_structure(data)


def test_delete_product(api_client):
    product_id = 5
    response = api_client.products.delete_product(product_id)

    assert response.status_code == 200
    assert_response_time(response)

    data = response.json()

    assert data["id"] == product_id
    assert data["isDeleted"] is True
