import pytest
from _pytest.capture import CaptureResult

from src.product import  Product
from src.category import Category
from src.Smartphone import Smartphone
from src.LawnGrass import LawnGrass

def test_print_mixin(capsys):
    Product.new_product("cheese", "Гауда", 600.00, 150)
    message = capsys.readouterr()
    # print(message)
    assert message == CaptureResult(out='Product(cheese, Гауда, 600.0, 150)\n', err='')


    LawnGrass.new_product(
        "Газонная трава 2",
        "Выносливая трава",
        450.0,
        15,
        "США",
        "5 дней",
        "Темно-зеленый",
    )
    message = capsys.readouterr()
    assert message == CaptureResult(out='LawnGrass(Газонная трава 2, Выносливая трава, 450.0, 15)\n', err='')

    Smartphone.new_product(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )
    message = capsys.readouterr()
    print(message)
    assert message == CaptureResult(out='Smartphone(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)\n', err='')