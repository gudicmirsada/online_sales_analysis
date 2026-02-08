from product import Product
from product_manager import ProductManager
from cart import Cart

def main():
    # Kreiranje ProductManager instance
    manager = ProductManager()

    # Kreiranje proizvoda
    product1 = Product("Laptop", 1200, 5)
    product2 = Product("Mouse", 25, 20)
    product3 = Product("Keyboard", 80, 10)

    # Dodavanje proizvoda u ProductManager
    manager.add_product(product1)
    manager.add_product(product2)
    manager.add_product(product3)

    # Kreiranje instance Cart
    cart = Cart()

    # Dodavanje proizvoda u korpu
    cart.add_to_cart(product1)
    cart.add_to_cart(product2)
    cart.add_to_cart(product3)

    # Prikaz korpe i ukupne vrijednosti
    cart.display_cart()
    print("Ukupna vrijednost korpe:", cart.total_cart_value())

if __name__ == "__main__":
    main()
