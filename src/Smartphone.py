from src.product import Product


class Smartphone(Product):
    def __init__(
        self, name, description, price, quantity, efficiency, model, memory, color
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    @classmethod
    def new_product(cls, name, description, price, quantity, efficiency, model, memory, color):
        return print(cls(name, description, price, quantity, efficiency, model, memory, color))
