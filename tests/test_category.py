import pytest
from src.сategory import Category
from src.product import Product


def test_category_init(category_food, category_toys):
    assert category_food.name == "Food"
    assert category_food.description == "Продукты питания"
    assert len(category_food.products) == 105
    assert category_toys.name == "Toys"
    assert category_toys.description == "Детские игрушки"
    assert len(category_toys.products) == 104

    assert Category.category_count == 2
    assert Category.product_count == 6


# тестирование геттера
def test_products_property(category_food):
    assert (
        (category_food.products)
        == "cheese, 600.0 руб. Остаток: 150 шт.\nmilk, 100.0 руб. Остаток: 300 шт.\ncoffe, 1800.0 руб. Остаток: 20 шт.\n"
    )


# тестирование сеттера
def test_products_setter(category_food):
    assert len(category_food.products) == 105


def test_category_add(category_food):
    assert str(category_food) == "Food, количество продуктов: 470 шт.\n"
