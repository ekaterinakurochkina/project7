from operator import add

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


def test_product_str(product_cheese):
    assert str(product_cheese) == "cheese, 600.0 руб. Остаток: 150 шт."


def test_product_add(product_cheese, product_milk):
    assert add(product_cheese, product_milk) == 120000.0