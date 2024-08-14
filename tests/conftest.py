import pytest
from src.category import Category
from src.product import Product
from src.Smartphone import Smartphone
from src.LawnGrass import LawnGrass


@pytest.fixture()
def category_food():
    return Category(
        name="Food",
        description="Продукты питания",
        products=[
            Product("cheese", "Гауда", 600.00, 150),
            Product("milk", "Первый вкус", 100.00, 300),
            Product("coffe", "Арабика", 1800.00, 20),
        ],
    )


import pytest
from src.product import Product
from src.category import Category


@pytest.fixture()
def category_food():
    return Category(
        name="Food",
        description="Продукты питания",
        products=[
            Product("cheese", "Гауда", 600.00, 150),
            Product("milk", "Первый вкус", 100.00, 300),
            Product("coffe", "Арабика", 1800.00, 20),
        ],
    )


@pytest.fixture()
def category_toys():
    return Category(
        name="Toys",
        description="Детские игрушки",
        products=[
            Product("ball", "Мяч надувной", 300.00, 80),
            Product("doll", "Кукла", 2100.00, 60),
            Product("tractor", "Синий трактор", 1500.00, 60),
        ],
    )

@pytest.fixture()
def product_list():
    return [
            Product("ball", "Мяч надувной", 300.00, 80),
            Product("doll", "Кукла", 2100.00, 60),
            Product("tractor", "Синий трактор", 1500.00, 60),
        ]


@pytest.fixture()
def product_cheese():
    return Product("cheese", "Гауда", 600.00, 150)


@pytest.fixture()
def product_toy():
    return Product("ball", "Мяч надувной", 300.00, 80)


@pytest.fixture()
def product_milk():
    return Product("milk", "Первый вкус", 100.00, 300)


@pytest.fixture()
def smartphone_init():
    return Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )


@pytest.fixture()
def lawn_grass_init():
    return LawnGrass(
        "Газонная трава 2",
        "Выносливая трава",
        450.0,
        15,
        "США",
        "5 дней",
        "Темно-зеленый",
    )


@pytest.fixture()
def product():
    return Product("cheese", "Гауда", 600.00, 150)
    # Product("milk", "Первый вкус", 100.00, 300)
