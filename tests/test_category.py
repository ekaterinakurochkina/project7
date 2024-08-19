import pytest
from src.category import Category
from src.product import Product
from operator import add


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


def test_add_prices(product_cheese, product_toy):
    assert add(product_cheese, product_toy) == 114000.0


# def test_add_product_list(category_toys):
#     assert Category.product_count == 3


def test_middle_price(category_toys, category_without_products):
    assert category_toys.middle_price() == 1300
    assert category_without_products.middle_price() == 0


# def test_products_list(category_toys):
#     assert (
#             (category_toys.products)
#             == 'ball, 300.0 руб. Остаток: 80 шт.\n'
#  'doll, 2100.0 руб. Остаток: 60 шт.\n'
#  'tractor, 1500.0 руб. Остаток: 60 шт.\n') != ('cheese, 600.0 руб. Остаток: 150 шт.\n'
#  'milk, 100.0 руб. Остаток: 300 шт.\n'
#  'coffe, 1800.0 руб. Остаток: 20 шт.\n'
#     )
#
# def test_add_product(product_list):
#     assert issubclass(type(product_list), Product) == False
#
# def test_add_valid_product(category_food):
#     new_product = Product('Product A', 10.0, 100.0, 15)
#     category_food.add_product(new_product)
#     assert len(category_food.products)== 143
#     assert str(category_food.products) == ('cheese, 600.0 руб. Остаток: 150 шт.\n'
#  'milk, 100.0 руб. Остаток: 300 шт.\n'
#  'coffe, 1800.0 руб. Остаток: 20 шт.\n'
#  'Product A, 100.0 руб. Остаток: 15 шт.\n')
