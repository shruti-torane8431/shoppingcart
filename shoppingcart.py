# Implement a Product class with attributes like product name, price, and quantity. Create a ShoppingCart class that
# can add products, remove products, and calculate the total cost.
# ===============================================================================================================
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - Price: {self.price}, Quantity: {self.quantity}"


class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_item(self, product):
        self.cart.append(product)
        print(f"Added {product.name} to the cart.")

    def remove_item(self, product_name):
        for product in self.cart:
            if product.name == product_name:
                self.cart.remove(product)
                print(f"Removed {product_name} from the cart.")
                return
        print(f"Product {product_name} not found in the cart.")

    def calculate_total(self):
        total = sum(product.price * product.quantity for product in self.cart)
        return total

    def show_cart(self):
        if not self.cart:
            print("The cart is empty.")
        else:
            print("Items in the cart:")
            for product in self.cart:
                print(product)


def main():
    cart = ShoppingCart()

    while True:
        print("\n1. Add Product")
        print("2. Remove Product")
        print("3. Show Cart")
        print("4. Calculate Total")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            product = Product(name, price, quantity)
            cart.add_item(product)


        elif choice == '2':
            product_name = input("Enter the name of the product to remove: ")
            cart.remove_item(product_name)

        elif choice == '3':
            cart.show_cart()

        elif choice == '4':
            total = cart.calculate_total()
            print(f"Total cost of items in the cart: ${total:.2f}")

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()