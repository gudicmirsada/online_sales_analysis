from product import Product
from product_manager import ProductManager
from cart import Cart  # import mora biti na vrhu fajla

def main():
    manager = ProductManager()

    product1 = Product("Laptop", 1200, 5)
    product2 = Product("Mouse", 25, 20)
    product3 = Product("Keyboard", 80, 10)

    # Dodavanje proizvoda u ProductManager
    manager.add_product(product1)
    manager.add_product(product2)
    manager.add_product(product3)

    # Prikaz proizvoda i ukupne vrijednosti inventara
    manager.display_products()
    print("Total inventory value:", manager.total_inventory_value())

    # Kreiranje instance Cart
    cart = Cart()

    # Dodavanje proizvoda u korpu
    cart.add_to_cart(product1)
    cart.add_to_cart(product2)
    cart.add_to_cart(product3)

    # Prikaz sadržaja korpe i ukupne vrijednosti
    cart.display_cart()
    print("Total cart value:", cart.total_cart_value())

if __name__ == "__main__":
    main()
