import pytest

from src.main import Category, Product


def test_product_init(product_cheese):
    assert product_cheese.name == "cheese"
    assert product_cheese.description == "Гауда"
    assert product_cheese.price == 600.00
    assert product_cheese.quantity == 150


def test_category_init(category_food, category_toys):
    assert category_food.name == "Food"
    assert category_food.description == "Продукты питания"
    assert len(category_food.products) == 3
    assert category_toys.name == "Toys"
    assert category_toys.description == "Детские игрушки"
    assert len(category_toys.products) == 3

    assert Category.category_count == 2
    assert Category.product_count == 6
