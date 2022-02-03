import datetime


def outdated_products(products: dict):
    return [product for product in products if products[product] < datetime.date.today()]
