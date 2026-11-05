from app import get_product_details, list_products


def test_product_listing():
    assert len(list_products()) == 3


def test_product_details():
    product = get_product_details(2)
    assert product["name"] == "Smartphone"
    assert product["price"] == 25000