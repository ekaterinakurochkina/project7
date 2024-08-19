import pytest
from src.product import Product
from src.Smartphone import Smartphone


def test_smartphone(smartphone_init):
    assert smartphone_init.name == "Samsung Galaxy S23 Ultra"
    assert smartphone_init.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone_init.price == 180000.0
    assert smartphone_init.quantity == 5
    assert smartphone_init.efficiency == 95.5
    assert smartphone_init.model == "S23 Ultra"
    assert smartphone_init.memory == 256
    assert smartphone_init.color == "Серый"
