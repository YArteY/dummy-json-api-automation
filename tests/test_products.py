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
    assert response.elapsed.total_seconds() < 2

    data = response.json()
    assert "products" in data
    assert "total" in data
    assert "skip" in data
    assert "limit" in data

    assert isinstance(data["products"], list)
    assert isinstance(data["total"], int)
    assert isinstance(data["skip"], int)
    assert isinstance(data["limit"], int)

    product = data['products'][0]

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
def test_sucess_get_product_by_id():
    product_id = 5
    response = api.products.get_product_by_id(product_id)

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == product_id
    assert isinstance(data["id"], int)
    assert "title" in data
    assert "price" in data
    assert "category" in data

    assert response.elapsed.total_seconds() < 2

def test_failed_get_product_by_id():
    product_id = 45489
    response = api.products.get_product_by_id(product_id)
    assert response.status_code == 404
    assert response.elapsed.total_seconds() < 2

def test_sucess_search_products():

    response = api.products.search_products(query="samsung")

    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 2

    data = response.json()

    assert "products" in data
    assert "total" in data
    assert "skip" in data
    assert "limit" in data

    assert isinstance(data["products"], list)
    assert isinstance(data["total"], int)
    assert isinstance(data["skip"], int)
    assert isinstance(data["limit"], int)

    product = data['products'][0]

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

def test_failed_search_products():
    response = api.products.search_products(query="GTA VI")

    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 2

    data = response.json()

    assert "products" in data
    assert data["total"] == 0
    assert data["skip"] == 0
    assert data["limit"] == 0

def test_get_all_categories():
    response = api.products.get_all_categories()

    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 2

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0

    category = data[0]

    assert "slug" in category
    assert "name" in category
    assert "url" in category

    assert isinstance(category["slug"], str)
    assert isinstance(category["name"], str)
    assert isinstance(category["url"], str)


def test_get_success_products_by_category():
    response = api.products.get_products_by_category(category="smartphones")

    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 2

    data = response.json()

    assert "products" in data
    assert "total" in data
    assert "skip" in data
    assert "limit" in data

    assert isinstance(data["products"], list)
    assert isinstance(data["total"], int)
    assert isinstance(data["skip"], int)
    assert isinstance(data["limit"], int)

    product = data['products'][0]

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

def test_failed_get_products_by_category():
    response = api.products.get_products_by_category(category="")

    assert response.status_code == 404
    assert response.elapsed.total_seconds() < 2

def test_success_add_product():
    payload = {
            "title": "iPhone 16",
            "description": "the perfect balance of price and quality",
            "price": 800,
            "category": "smartphones"
        }
    response = api.products.add_product(payload)

    assert response.status_code == 201
    assert response.elapsed.total_seconds() < 2

    data = response.json()

    assert "id" in data
    assert "title" in data
    assert "description" in data
    assert "price" in data
    assert "category" in data

    assert isinstance(data["id"], int)
    assert isinstance(data["title"], str)
    assert isinstance(data["description"], str)
    assert isinstance(data["price"], (int, float))
    assert isinstance(data["category"], str)

def test_update_product():
    product_id = 5
    payload = {
        "title": "iPhone 16",
        "description": "the perfect balance of price and quality",
        "price": 800,
        "category": "smartphones"
    }
    response = api.products.update_product(product_id, payload)

    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 2

    data = response.json()

    assert "id" in data
    assert data["title"] == payload["title"]
    assert data["description"] == payload["description"]
    assert data["price"] == payload["price"]
    assert data["category"] == payload["category"]

    assert isinstance(data["id"], int)
    assert isinstance(data["title"], str)
    assert isinstance(data["description"], str)
    assert isinstance(data["price"], (int, float))
    assert isinstance(data["category"], str)

def test_patch_product():
    product_id = 5
    payload = {
        "title": "iPhone 16",
    }
    response = api.products.patch_product(product_id, payload)

    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 2

    data = response.json()

    assert "id" in data
    assert data["title"] == payload["title"]
    assert "description" in data
    assert "price" in data
    assert "category" in data

    assert isinstance(data["id"], int)
    assert isinstance(data["title"], str)
    assert isinstance(data["description"], str)
    assert isinstance(data["price"], (int, float))
    assert isinstance(data["category"], str)

def test_delete_product():
    product_id = 5
    response = api.products.delete_product(product_id)

    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 2

    data = response.json()

    assert data["id"] == product_id
    assert data["isDeleted"] is True





