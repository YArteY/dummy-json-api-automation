from utils.config import MAX_RESPONSE_TIME_SECONDS


def assert_response_time(response, max_seconds=MAX_RESPONSE_TIME_SECONDS):
    """Valida que la respuesta llegue dentro del tiempo máximo configurado."""
    assert response.elapsed.total_seconds() < max_seconds


def assert_product_structure(product):
    """Valida la estructura de un producto individual."""
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


def assert_product_list_structure(data):
    """Valida la estructura de una respuesta de listado de productos."""
    assert "products" in data
    assert "total" in data
    assert "skip" in data
    assert "limit" in data

    assert isinstance(data["products"], list)
    assert isinstance(data["total"], int)
    assert isinstance(data["skip"], int)
    assert isinstance(data["limit"], int)

    if data["products"]:
        assert_product_structure(data["products"][0])


def assert_category_structure(category):
    """Valida la estructura de una categoría."""
    assert "slug" in category
    assert "name" in category
    assert "url" in category

    assert isinstance(category["slug"], str)
    assert isinstance(category["name"], str)
    assert isinstance(category["url"], str)


def assert_user_structure(user):
    """Valida la estructura de un usuario."""
    assert "id" in user
    assert "firstName" in user
    assert "lastName" in user
    assert "username" in user
    assert "email" in user

    assert isinstance(user["id"], int)
    assert isinstance(user["firstName"], str)
    assert isinstance(user["lastName"], str)
    assert isinstance(user["username"], str)
    assert isinstance(user["email"], str)
