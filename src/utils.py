import json
import os
from ast import Str
from typing import Dict


from src.product import Product
from src.сategory import Category


def read_json(path: Str) -> Dict:
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="Utf-8") as file:
        data = json.load(file)
    return data


def create_objects_from_json(data):
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))
    return categories


if __name__ == "__main__":
    raw_data = read_json("../data/products.json")
    print(raw_data)
    data_categories = create_objects_from_json(raw_data)
    print(data_categories)
    print(data_categories[0].name)
    print(data_categories[0].description)
    print(data_categories[0].products)
