class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def display(self):
        return f"ID: {self.product_id}, Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}"

class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def add_product(self):
        product_id = int(input("Enter Product ID: "))
        name = input("Enter Product Name: ")
        price = float(input("Enter Product Price: "))
        quantity = int(input("Enter Product Quantity: "))
        product = Product(product_id, name, price, quantity)
        
        if product.product_id in self.cart:
            self.cart[product.product_id].quantity += product.quantity
        else:
            self.cart[product.product_id] = product
        print(f"{product.name} added to cart.")

    def remove_product(self):
        product_id = int(input("Enter Product ID to remove: "))
        if product_id in self.cart:
            removed_product = self.cart.pop(product_id)
            print(f"{removed_product.name} removed from cart.")
        else:
            print("Product not found in cart.")

    def display_cart(self):
        if not self.cart:
            print("Shopping cart is empty.")
        else:
            print("Shopping Cart:")
            for product in self.cart.values():
                print(product.display())

# Example Usage
if __name__ == "__main__":
    cart = ShoppingCart()
    while True:
        print("\n1. Add Product\n2. Remove Product\n3. Display Cart\n4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            cart.add_product()
        elif choice == "2":
            cart.remove_product()
        elif choice == "3":
            cart.display_cart()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")
