from product import Product

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_products(self):
        for product in self.products:
            print(product.display_info())

    def total_inventory_value(self):
        total = 0
        for product in self.products:
            total += product.price * product.quantity
        return total
    def remove_product_by_name(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                return True
        return False
