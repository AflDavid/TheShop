import datetime
import random
from abc import ABC, abstractmethod


class ToolItem:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def reduce_stock(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
            return True
        else:
            print(f"Insufficient stock for {self.name}. Available stock: {self.stock}")
            return False


class CartItem:
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity


class Catalogue:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def display_catalogue(self):
        print("Catalogue:")
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item.name} - ${item.price:.2f} - Stock: {item.stock}")

    def get_item(self, index):
        if 1 <= index <= len(self.items):
            return self.items[index - 1]
        else:
            return None


class CartItemObserver(ABC):
    @abstractmethod
    def update(self):
        pass


class CartSubject:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update()


class Cart(CartSubject):
    def __init__(self):
        super().__init__()
        self.items = []

    def add_item(self, item, quantity):
        if item.reduce_stock(quantity):
            cart_item = CartItem(item, quantity)
            self.items.append(cart_item)
            self.notify_observers()

    def remove_item(self, index):
        if 1 <= index <= len(self.items):
            item = self.items[index - 1].item
            item.stock += self.items[index - 1].quantity
            del self.items[index - 1]
            self.notify_observers()

    def update_quantity(self, index, quantity):
        if 1 <= index <= len(self.items):
            item = self.items[index - 1].item
            item.stock += self.items[index - 1].quantity
            self.items[index - 1].quantity = quantity
            item.reduce_stock(quantity)
            self.notify_observers()

    def display_cart(self):
        print("Cart:")
        for i, cart_item in enumerate(self.items, 1):
            item = cart_item.item
            quantity = cart_item.quantity
            print(f"{i}. {item.name} - ${item.price:.2f} x {quantity}")

    def get_total_price(self):
        total = 0
        for cart_item in self.items:
            item = cart_item.item
            quantity = cart_item.quantity
            total += item.price * quantity
        return total


class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, total_price):
        pass


class TenPercentDiscount(DiscountStrategy):
    def apply_discount(self, total_price):
        return total_price * 0.1


class Shipment:
    def __init__(self, address, shipping_method):
        self.address = address
        self.shipping_method = shipping_method

    def display_shipment_info(self):
        print("Shipping Address:", self.address)
        print("Shipping Method:", self.shipping_method)


class OrderFacade:
    def __init__(self, catalogue, cart, shipment):
        self.catalogue = catalogue
        self.cart = cart
        self.shipment = shipment

    def add_item_to_cart(self, item_index, quantity):
        item = self.catalogue.get_item(item_index)
        if item:
            self.cart.add_item(item, quantity)
            print("Tool added to cart.")
        else:
            print("Invalid item number.")

    def remove_item_from_cart(self, item_index):
        self.cart.remove_item(item_index)
        print("Tool removed from cart.")

    def update_item_quantity(self, item_index, new_quantity):
        self.cart.update_quantity(item_index, new_quantity)
        print("Tool quantity updated.")

    def process_order(self, payment_method, discount_strategy):
        if not self.cart.items:
            print("Cannot process order. Cart is empty.")
            return

        total_price = self.cart.get_total_price()
        print(f"Total price: ${total_price:.2f}")

        discount_amount = 0
        if discount_strategy:
            discount_amount = discount_strategy.apply_discount(total_price)
            total_price -= discount_amount
            print(f"Discount applied: {discount_strategy.__class__.__name__}")
            print(f"Discount amount: ${discount_amount:.2f}")

        print(f"\nTotal price (after discount): ${total_price:.2f}")

        address = input("Enter shipping address: ")
        shipping_method = input("Enter shipping method: ")
        shipment = Shipment(address, shipping_method)
        self.shipment = shipment

        print("\nOrder Summary:")
        self.cart.display_cart()
        print()
        shipment.display_shipment_info()

        print("\nPayment Summary:")
        print("Payment method:", payment_method)
        print(f"Total price (after discount): ${total_price:.2f}")

        self.generate_receipt(payment_method, discount_strategy)

        # Reset the cart after completing the checkout
        self.cart.items.clear()

    def generate_receipt(self, payment_method, discount_strategy):
        order_id = random.randint(1000, 9999)
        current_datetime = datetime.datetime.now()

        print("\nReceipt:")
        print("Order ID:", order_id)
        print("Date:", current_datetime.strftime("%Y-%m-%d"))
        print("Time:", current_datetime.strftime("%H:%M:%S"))
        print()

        self.cart.display_cart()
        total_price = self.cart.get_total_price()

        if discount_strategy:
            print(f"\nDiscount applied: {discount_strategy.__class__.__name__}")
            print(f"Discount amount: ${discount_strategy.apply_discount(total_price):.2f}")

        print(f"\nTotal price (after discount): ${total_price:.2f}")
        print("Payment method:", payment_method)

        print("\nShipment Details:")
        self.shipment.display_shipment_info()

        with open("order_log.txt", "a") as log_file:
            log_file.write(f"Order ID: {order_id}\n")
            log_file.write(f"Date: {current_datetime.strftime('%Y-%m-%d')}\n")
            log_file.write(f"Time: {current_datetime.strftime('%H:%M:%S')}\n")
            log_file.write("Items:\n")
            for cart_item in self.cart.items:
                item = cart_item.item
                quantity = cart_item.quantity
                log_file.write(f"{item.name} - ${item.price:.2f} x {quantity}\n")
            log_file.write(f"Total price: ${total_price:.2f}\n")
            log_file.write("Payment method: " + payment_method + "\n")
            log_file.write("Shipment Address: " + self.shipment.address + "\n")
            log_file.write("Shipment Method: " + self.shipment.shipping_method + "\n")
            log_file.write("\n")


class CartObserver(CartItemObserver):
    def __init__(self, cart):
        self.cart = cart

    def update(self):
        print("Cart updated. Total price: ${:.2f}".format(self.cart.get_total_price()))


class OrderMediator:
    def __init__(self, catalogue, cart, facade):
        self.catalogue = catalogue
        self.cart = cart
        self.facade = facade

    def order_item(self, item_index, quantity):
        self.facade.add_item_to_cart(item_index, quantity)

    def remove_item(self, item_index):
        self.facade.remove_item_from_cart(item_index)

    def update_quantity(self, item_index, new_quantity):
        self.facade.update_item_quantity(item_index, new_quantity)


class AddToCartCommand:
    def __init__(self, mediator, item_index, quantity):
        self.mediator = mediator
        self.item_index = item_index
        self.quantity = quantity

    def execute(self):
        self.mediator.order_item(self.item_index, self.quantity)


class Seller:
    def __init__(self, catalogue):
        self.catalogue = catalogue

    def display_seller_menu(self):
        while True:
            print("\nSeller Menu:")
            print("1. Display Catalogue")
            print("2. Add New Tool")
            print("3. Update Tool Stock")
            print("4. Update Tool Price")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.catalogue.display_catalogue()
            elif choice == "2":
                self.add_new_tool()
            elif choice == "3":
                self.update_tool_stock()
            elif choice == "4":
                self.update_tool_price()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")

    def add_new_tool(self):
        name = input("Enter tool name: ")
        price = float(input("Enter tool price: "))
        stock = int(input("Enter tool stock: "))
        new_tool = ToolItem(name, price, stock)
        self.catalogue.add_item(new_tool)
        print("Tool added to the catalogue.")

    def update_tool_stock(self):
        self.catalogue.display_catalogue()
        tool_index = int(input("Enter the tool number to update stock: "))
        tool = self.catalogue.get_item(tool_index)
        if tool:
            new_stock = int(input("Enter the new stock: "))
            tool.stock = new_stock
            print(f"{tool.name} stock updated to {new_stock}.")
        else:
            print("Invalid tool number.")

    def update_tool_price(self):
        self.catalogue.display_catalogue()
        tool_index = int(input("Enter the tool number to update price: "))
        tool = self.catalogue.get_item(tool_index)
        if tool:
            new_price = float(input("Enter the new price: "))
            tool.price = new_price
            print(f"{tool.name} price updated to ${new_price:.2f}.")
        else:
            print("Invalid tool number.")


def main():
    catalogue = Catalogue()
    catalogue.add_item(ToolItem("Hammer", 15.99, 10))
    catalogue.add_item(ToolItem("Screwdriver", 8.99, 15))
    catalogue.add_item(ToolItem("Wrench", 12.99, 8))
    catalogue.add_item(ToolItem("Pliers", 7.99, 12))

    cart = Cart()
    cart_observer = CartObserver(cart)
    cart.add_observer(cart_observer)

    shipment = Shipment("", "")
    order_facade = OrderFacade(catalogue, cart, shipment)
    order_mediator = OrderMediator(catalogue, cart, order_facade)

    seller = Seller(catalogue)

    while True:
        print("\n1. Display Catalogue")
        print("2. Add Tool to Cart")
        print("3. Remove Tool from Cart")
        print("4. Update Tool Quantity")
        print("5. Display Cart")
        print("6. Checkout")
        print("7. Cancel Order")
        print("8. Continue Shopping")
        print("9. Seller Menu")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            catalogue.display_catalogue()
        elif choice == "2":
            catalogue.display_catalogue()
            item_index = int(input("Enter the tool number: "))
            quantity = int(input("Enter the quantity: "))
            add_to_cart_command = AddToCartCommand(order_mediator, item_index, quantity)
            add_to_cart_command.execute()
        elif choice == "3":
            cart.display_cart()
            item_index = int(input("Enter the tool number: "))
            order_mediator.remove_item(item_index)
        elif choice == "4":
            cart.display_cart()
            item_index = int(input("Enter the tool number: "))
            new_quantity = int(input("Enter the new quantity: "))
            order_mediator.update_quantity(item_index, new_quantity)
        elif choice == "5":
            cart.display_cart()
            total_price = cart.get_total_price()
            print(f"Total price: ${total_price:.2f}")
        elif choice == "6":
            total_price = cart.get_total_price()
            if total_price == 0:
                print("Cart is empty. Please add tools to the cart.")
                continue

            print(f"Total price: ${total_price:.2f}")

            discount_code = input("Enter discount code (leave blank for no discount): ")
            payment_methods = ["Cash", "Credit Card", "PayPal"]
            print("Select a payment method:")
            for i, method in enumerate(payment_methods, 1):
                print(f"{i}. {method}")

            payment_choice = input("Enter your payment choice: ")
            payment_choice = int(payment_choice)

            if 1 <= payment_choice <= len(payment_methods):
                payment_method = payment_methods[payment_choice - 1]
                order_facade.process_order(payment_method, TenPercentDiscount())
            else:
                print("Invalid payment choice.")
        elif choice == "7":
            cart.items.clear()
            print("Order cancelled. Cart is now empty.")
        elif choice == "8":
            # Continue shopping, reset the cart
            cart.items.clear()
        elif choice == "9":
            seller.display_seller_menu()
        elif choice == "10":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
     main()
