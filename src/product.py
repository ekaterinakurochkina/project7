from typing import Any
from src.BaseProduct import BaseProduct
from src.print_mixin import PrintMixin

class Product(BaseProduct, PrintMixin):
    """Класс для представления продукта"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__(name, description, price, quantity)

    # def __str__(self):
    #     """Метод преобразования данных о классе в строку"""
    #     return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Метод, позволяющий рассчитать стоимость продуктов, имеющихся на складе"""
        return self.quantity * self.__price + other.quantity * other.__price

    # метод добавления объекта класса из словаря
    @classmethod
    def new_product_from_dict(cls, dict_product: dict):
        return cls(
            name=dict_product.get("name"),
            description=dict_product.get("description"),
            price=dict_product.get("price"),
            quantity=dict_product.get("quantity"),
        )

    @classmethod
    def new_product(cls, name, description, price, quantity):
        return print(cls(name, description, price, quantity))


    # Для класса Product опишите геттеры и сеттеры
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price <= 0:
            print(
                f"Новая цена: {new_price}\nЦена не должна быть нулевой или отрицательной."
            )
        elif new_price < self.__price:
            user_choice = input(
                f"Новая цена: {new_price}\nВы подтверждаете понижение цены? y/n\n"
            ).lower()
            if user_choice == "y":
                self.__price = new_price
        else:
            self.__price = new_price
