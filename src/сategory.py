from src.product import Product


class Category:
    """Класс для представления категории"""

    name: str
    description: str
    products: list  # это СПИСОК продуктов

    category_count = 0  # Переменная на уровне класса для подсчета количества категорий
    product_count = 0  # Переменная на уровне класса для подсчета количества товаров

    def __init__(self, name, description, products=None):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__products = products if products else []  # это СПИСОК продуктов
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def add_product(self, new_product: Product):
        self.__products.append(new_product)
        # self.product_count +=1

    # Геттер, который выводит список товаров в виде строк в формате:
    # Название продукта, 80 руб. Остаток: 15 шт
    @property
    def products(self):
        products_str = ""
        for product in self.__products:
            products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт. \n"
            self.product_count += 1
        return products_str

    # # Геттер и сеттер для добавления нового товара -  почему-то в таком виде код не работает
    # @property
    # def add_product(self, new_product: Product) -> Product:
    #     return self.__products
    #
    # @add_product.setter
    # def add_product(self, new_product: Product):
    #     self.__products.append(self, new_product)
    #     Category.product_count += 1
