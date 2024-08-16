from abc import ABC, abstractmethod

class BaseProduct(ABC):
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity


    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        pass


