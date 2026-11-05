PRODUCTS = [
    {"id": 1, "name": "Laptop", "price": 55000},
    {"id": 2, "name": "Smartphone", "price": 25000},
    {"id": 3, "name": "Headphones", "price": 3000},
]


def list_products():
    return PRODUCTS


def get_product_details(product_id):
    for product in PRODUCTS:
        if product["id"] == product_id:
            return product
    return None

def filter_products(keyword):
    keyword = keyword.strip().lower()
    return [
        product
        for product in PRODUCTS
        if keyword in product["name"].lower()
    ]

