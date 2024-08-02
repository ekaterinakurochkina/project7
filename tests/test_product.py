import pytest
from src.product import Product


def test_product_init(product_cheese):
    assert product_cheese.name == "cheese"
    assert product_cheese.description == "Гауда"
    assert product_cheese.price == 600.00
    assert product_cheese.quantity == 150