"""
Retail Store Management System: A module for handling operations
related to a retail store, such as managing members, items,
inventory, and transactions.
"""


class Member:
    """
    Represents a member of the store with a name and a purchase history.
    """

    def __init__(self, name):
        self.name = name
        self.purchase_history = []

    def update_name(self, new_name):
        """
        Updates the name of the member.
        """

        self.name = new_name

    def add_purchase(self, item):
        """
        Adds an item to the member's purchase history.
        """
        self.purchase_history.append(item)


class Item:
    """
    Represents an item in the store's inventory.
    """

    def __init__(self, item_name, price, stock, category):
        self.item_name = item_name
        self.price = price
        self.stock = stock
        self.category = category

    def update_stock(self, amount):
        """
        Updates the stock of the item.
        """

        self.stock += amount

    def update_price(self, new_price):
        """
        Updates the price of the item.
        """

        self.price = new_price


class Category:
    """
    Represents a category of items in the store.
    """

    def __init__(self, name):
        self.name = name
        self.items = {}

    def add_item(self, item):
        """
        Adds an item to the category.
        """

        self.items[item.item_name] = item

    def remove_item(self, item_name):
        """
        Removes an item from the category.
        """

        if item_name in self.items:
            del self.items[item_name]

    def list_items(self):
        """
        Lists all items in the category.
        """

        return self.items.values()


class Inventory:
    """
    Manages the inventory of items in the store.
    """

    def __init__(self):
        self.items = {}

    def add_item(self, item):
        """
        Adds an item to the inventory.
        """

        self.items[item.item_name] = item

    def remove_item(self, item_name):
        """
        Removes an item from the inventory.
        """
        if item_name in self.items:
            del self.items[item_name]

    def search_item(self, item_name):
        """
        Searches for an item in the inventory.
        """

        return self.items.get(item_name, None)

    def list_items_by_category(self, category):
        """
        Lists items in the inventory by a specific category.
        """
        return category.list_items()


class Transaction:
    """
    Handles a transaction for a store member.
    """

    def __init__(self, member, order_items):
        self.member = member
        self.items = order_items
        self.total = sum(item.price for item in order_items)


    def add_item(self, item):
        """
        Adds an item to the transaction.
        """

        self.items.append(item)
        self.total += item.price

    def remove_item(self, item):
        """
        Removes an item from the transaction.
        """

        if item in self.items:
            self.items.remove(item)
            self.total -= item.price

    def process(self):
        """
        Processes the transaction by updating item stocks and member's purchase history.
        Outputs a message if an item is out of stock.
        """
        for item in self.items:
            if item.stock > 0:
                item.stock -= 1
                self.member.add_purchase(item)
            else:
                print(f"Sorry, {item.item_name} is out of stock.")


members = {}
items = {}
categories = {}
inventory = Inventory()


def member_management():
    """
    Manages member-related operations such as adding, updating members,
    and viewing purchase history.
    """

    while True:
        print("\nMember Management:")
        print("1. Add Member")
        print("2. Update Member")
        print("3. View Purchase History")
        print("4. Return to Main Menu")
        choice = input("Enter choice: ")

        if choice == "1":
            member_name = input("Enter Member Name: ")
            members[member_name] = Member(member_name)
            print(f"Member {member_name} added successfully!")

        elif choice == "2":
            member_name = input("Enter Member Name to Update: ")
            if member_name in members:
                new_name = input("Enter New Name: ")
                members[new_name] = members.pop(member_name)
                print(f"Member {member_name} updated to {new_name}!")
            else:
                print(f"Member {member_name} doesn't exist, so it can't be updated.")

        elif choice == "3":
            member_name = input("Enter Member Name: ")
            if member_name in members:
                purchases = members[member_name].purchase_history
                if purchases:
                    print(f"\nPurchases for {member_name}:")
                    item_counts = {}
                    for purchase in purchases:
                        if purchase.item_name in item_counts:
                            item_counts[purchase.item_name] += 1
                        else:
                            item_counts[purchase.item_name] = 1

                    for item_name, count in item_counts.items():
                        print(f"{count} - {item_name}")
                else:
                    print("No purchases found!")
            else:
                print("Member not found!")

        elif choice == "4":
            break


def item_management():
    """
    Manages item-related operations such as adding and removing items,
    and viewing categories.
    """

    while True:
        print("\nItem Management:")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. View Categories")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            item_name = input("Enter Item Name: ")
            item_price = float(input("Enter Item Price: "))
            item_stock = int(input("Enter Item Stock: "))
            category_name = input("Enter Category Name: ")

            # Check for category existence or create a new one
            if category_name not in categories:
                categories[category_name] = Category(category_name)

            item = Item(item_name, item_price, item_stock,
                        categories[category_name])

            # Add item to category and inventory
            categories[category_name].add_item(item)
            inventory.add_item(item)
            print(
                f"Item {item_name} added to category {category_name} and inventory successfully!")

        elif choice == "2":
            item_name = input("Enter Item Name to Remove: ")
            found = False
            for category in categories.values():
                if item_name in category.items:
                    category.remove_item(item_name)
                    found = True
                    break
            if found:
                inventory.remove_item(item_name)
                print(f"Item {item_name} removed successfully!")
            else:
                print("Item not found!")

        elif choice == "3":
            if not categories:
                print("\nNo categories or items in inventory.")
            else:
                print("\nCategories and Items:")
                for category_name, category in categories.items():
                    print(f"\n{category_name}:")
                    for item in category.list_items():
                        print(
                            f"  - {item.item_name}: ${item.price}, Stock: {item.stock}")

        elif choice == "4":
            break


def view_inventory():
    """
    Provides options for viewing the inventory either based on items
    or categories.
    """
    while True:
        print("\nInventory Viewing:")
        print("1. Search Based On Item")
        print("2. Search Based on Categories")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            item_name = input("Enter Item Name: ")
            item = inventory.search_item(item_name)
            if item:
                print(f"{item_name}: ${item.price}, "
                      f"Stock: {item.stock}, Category: {item.category.name}")
            else:
                print("Item not found!")

        elif choice == "2":
            category_name = input("Enter Category Name: ")
            if category_name in categories:
                items_in_category = inventory.list_items_by_category(
                    categories[category_name])
                for item in items_in_category:
                    print(f"{item.item_name}: ${item.price}, Stock: {item.stock}")
            else:
                print("Category not found!")

        elif choice == "3":
            break


def transaction_processing():
    """
    Processes a transaction including item selection and purchase by a member.
    """

    member_name = input("\nEnter Member Name: ")
    if member_name not in members:
        print("Member not found!")
        return

    items_to_purchase = []
    total_cost = 0.0

    while True:
        print("\nInventory:")
        for index, (item_name, item) in enumerate(inventory.items.items(), 1):
            print(f"{index}. {item_name}: ${item.price}, Stock: {item.stock}")

        try:
            item_choice = int(
                input("\nEnter The Item to Purchase or 0 to finish: "))

            if item_choice == 0:
                break

            item_name = list(inventory.items.keys())[item_choice - 1]

            item = inventory.items[item_name]
            if item.stock <= 0:
                print(f"Sorry, {item_name} is out of stock!")
                continue

            quantity = int(
                input(f"How many {item_name}s would you like to purchase? "))
            if quantity > item.stock:
                print(f"Sorry, only {item.stock} {item_name}s are in stock!")
                continue

            item.stock -= quantity
            total_cost += item.price * quantity
            items_to_purchase.extend([item] * quantity)
        except (ValueError, IndexError):
            print("Invalid selection! Please try again.")

    if not items_to_purchase:
        print("No items selected for purchase.")
        return

    for item in items_to_purchase:
        members[member_name].add_purchase(item)

    print(f"\nTotal cost of items: ${total_cost:.2f}")
    print(f"Items purchased successfully by {member_name}!")


def main():
    """
    The main function to run the Retail Store Management Program.
    Offers different management options like Member, Item, Inventory,
    and Transaction Management.
    """

    while True:
        print("\nWelcome to the Retail Store Management Program!")
        print("1. Member Management")
        print("2. Item Management")
        print("3. Inventory Viewing")
        print("4. Transaction Processing")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            member_management()

        elif choice == "2":
            item_management()

        elif choice == "3":
            view_inventory()

        elif choice == "4":
            transaction_processing()

        elif choice == "5":
            print("\nThank you for using the Retail Store Management Program!")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
