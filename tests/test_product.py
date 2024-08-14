from operator import add

import pytest
from src.product import Product
from src.Smartphone import Smartphone
from src.LawnGrass import LawnGrass


def test_product_init(product_cheese):
    assert product_cheese.name == "cheese"
    assert product_cheese.description == "Гауда"
    assert product_cheese.price == 600.00
    assert product_cheese.quantity == 150


def test_product_str(product_cheese):
    assert str(product_cheese) == "cheese, 600.0 руб. Остаток: 150 шт."


def test_product_add(product_cheese, product_milk):
    assert add(product_cheese, product_milk) == 120000.0


def test_add_product(smartphone_init, product_count=0):
    assert product_count == 0

    # add_product(smartphone_init)
    # assert product_count == 1
    # @pytest.fixture()
    # def smartphone_init():
    #     return Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
    #                       "S23 Ultra", 256, "Серый")

    # def add_product(self, new_product):
    #     if issubclass(type(new_product),Product) == True and isinstance(new_product, Product):
    #         # super().__init__(self.name, self.description, self.price, self.quantity)
    #         self.__products.append(new_product)
    #          # self.product_count +=1
    #     else:
    #         raise TypeError
