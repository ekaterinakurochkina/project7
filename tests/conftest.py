import pytest
from src.main import Product, Category


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
def product_cheese():
    return Product("cheese", "Гауда", 600.00, 150)
