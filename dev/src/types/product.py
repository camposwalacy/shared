from src.enums.enums import ProductType

class Product():
    def __init__(self, id, name, price):
        """
        This class is about handing product
        :param id: {str} Id of product
        :param name: {str} Name of product
        :param price: {float} Price value of product
        """
        self.id = id
        self.name = name
        self.price = price
        self.type = ProductType.UNKNOWN

