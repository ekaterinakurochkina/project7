import pytest
from src.product import Product


def test_product_init(product_cheese):
    assert product_cheese.name == "cheese"
    assert product_cheese.description == "Гауда"
    assert product_cheese.price == 600.00
    assert product_cheese.quantity == 150


def test_new_product():
    new_product = Product("ball", "Мяч надувной", 300.00, 80)
    new_product.name = "ball"
    new_product.description = "Мяч надувной"
    new_product.__price = 300.00
    new_product.quantity = 80
