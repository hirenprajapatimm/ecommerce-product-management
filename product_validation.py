from app import get_product_details, list_products

products = list_products()

assert len(products) == 3
assert all(product["price"] > 0 for product in products)
assert get_product_details(2)["name"] == "Smartphone"

print("Product validation passed")