from product import Product

class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product):
        self.cart_items.append(product)

    def total_cart_value(self):
        total = 0
        for item in self.cart_items:
            total += item.price * item.quantity
        return total

    def display_cart(self):
        print("Cart contents:")
        for item in self.cart_items:
            print(item.display_info())
