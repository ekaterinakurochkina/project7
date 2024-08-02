import pytest
from src.сategory import Category

def test_category_init(category_food, category_toys):
    assert category_food.name == "Food"
    assert category_food.description == "Продукты питания"
    assert len(category_food.products) == 3
    assert category_toys.name == "Toys"
    assert category_toys.description == "Детские игрушки"
    assert len(category_toys.products) == 3

    assert Category.category_count == 2
    assert Category.product_count == 6