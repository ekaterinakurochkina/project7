from src.product import Product
class Category():
    """Класс для представления категории"""

    name: str
    description: str
    products: list   # это СПИСОК продуктов

    category_count = 0  # Переменная на уровне класса для подсчета количества категорий
    product_count = 0  # Переменная на уровне класса для подсчета количества товаров

    def __init__(self, name, description, products):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__products = products    # это СПИСОК продуктов
        Category.category_count += 1
        Category.product_count += len(products) if products else 0


# специальный метод , в который нужно передавать объект класса Product,
# и уже его записывать в приватный атрибут списка товаров:
    @classmethod
    def add_product(cls,):
        new_product = Product()
        return new_product


# Геттер, который будет выводить список товаров в виде строк в формате:
# Название продукта, 80 руб. Остаток: 15 шт
    @property
    def products(self):
        products_list = ""
        for product in self.__products:
            products_list += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт. \n"
        return products_list