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

    def __str__(self):
        """Метод преобразования данных о классе в строку, суммирующий продукты в заданной категории"""
        product_count = 0
        for product in self.__products:
            product_count += product.quantity
        return f"{self.name}, количество продуктов: {product_count} шт.\n"


    def __add__(self, other):  # 16.1
        """Метод суммирования товаров в заданной категории"""
        if isinstance(other, Product):
            return (self.__price * self.quantity) + (other.__price * other.quantity)
        raise TypeError

    def add_product(self, new_product: Product):
        if issubclass(type(new_product), Product) == True and isinstance(
            new_product, Product
        ):
            self.__products.append(new_product)
        # self.product_count +=1
        else:
            raise TypeError
    def middle_price(self):
        """Метод нахождения средней цены товаров"""
        try:
            return sum([product.price for product in self.__products])/len(self.__products)
        except ZeroDivisionError:
            return 0



    # Геттер, который выводит список товаров:
    @property
    def products(self):
        products_str = ""
        for product in self.__products:
            products_str += f"{str(product)}\n"
            self.product_count += 1
        return products_str
