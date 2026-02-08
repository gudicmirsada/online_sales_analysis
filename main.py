from product import Product
from product_manager import ProductManager

def main():
    manager = ProductManager()

    product1 = Product("Laptop", 1200, 5)
    product2 = Product("Mis", 25, 20)
    product3 = Product("Tastatura", 80, 10)

    manager.add_product(product1)
    manager.add_product(product2)
    manager.add_product(product3)

    manager.display_products()
    print("Total inventory value:", manager.total_inventory_value())

if __name__ == "__main__":
    main()
