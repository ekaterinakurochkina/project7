import pytest
from src.product import Product
from src.LawnGrass import LawnGrass


def test_LawnGrass(lawn_grass_init):
    assert lawn_grass_init.name == "Газонная трава 2"
    assert lawn_grass_init.description == "Выносливая трава"
    assert lawn_grass_init.price == 450.0
    assert lawn_grass_init.quantity == 15
    assert lawn_grass_init.country == "США"
    assert lawn_grass_init.germination_period == "5 дней"
    assert lawn_grass_init.color == "Темно-зеленый"
