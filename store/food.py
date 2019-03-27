##File information
# food class
# 3/27/19
##endregion
from store.product import Product


class Food(Product):
    def __init__(self, product, rate):
        super().__init__(product.getCode(), product.getDescription(), product.getQuantity(), product.getPrice())
        self.__taxRate = rate

    def __init__(self, code, descrip, quant, price, rate):
        super().__init__(code, descrip, quant, price)
        self.__taxRate = rate