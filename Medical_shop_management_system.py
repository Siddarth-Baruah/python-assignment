# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 17:24:49 2024

@author: Lenovo
"""

from datetime import datetime

# Inventory dictionary to store the items
inventory = {}

# Function to add or update an item in the inventory
def add_item():
    print("\n--- Add or Update Item ---")
    
    name = input("Enter item name: ").strip()
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per unit: "))
    expiry_date = input("Enter expiry date (dd-mm-yyyy): ").strip()
    
    # Convert expiry date string to date object
    expiry = datetime.strptime(expiry_date, "%d-%m-%Y")
    
    # If item exists, update its quantity and other details
    if name in inventory:
        inventory[name]['quantity'] += quantity
        inventory[name]['price'] = price
        inventory[name]['expiry'] = expiry
    else:
        # Add new item if it doesn't exist
        inventory[name] = {'quantity': quantity, 'price': price, 'expiry': expiry}
    
    print(f"\n'{name}' has been added/updated in the inventory.")

# Function to delete an item from inventory
def delete_item():
    print("\n--- Delete an Item ---")
    
    name = input("Enter the name of the item to delete: ").strip()
    
    # Check if the item exists in inventory
    if name in inventory:
        del inventory[name]
        print(f"\n'{name}' has been removed from the inventory.")
    else:
        print(f"\n'{name}' is not found in the inventory.")

# Function to search for an item in the inventory
def search_item():
    print("\n--- Search for an Item ---")
    
    name = input("Enter the name of the item to search: ").strip()
    
    # Check if item exists and display its details
    if name in inventory:
        item = inventory[name]
        print(f"\nItem: {name} | Quantity: {item['quantity']} | Price: ₹{item['price']:.2f} | Expiry: {item['expiry'].strftime('%d-%m-%Y')}")
    else:
        print(f"\n'{name}' is not found in the inventory.")

# Function to display items past their expiry date
def expired_items():
    print("\n--- List of Expired Items ---")
    
    current_date = datetime.now()
    expired = False
    
    for item, details in inventory.items():
        if details['expiry'] < current_date:
            print(f"Item: {item} | Quantity: {details['quantity']} | Expired on: {details['expiry'].strftime('%d-%m-%Y')}")
            expired = True
    
    if not expired:
        print("No expired items found.")

# Function to display all items in the inventory
def display_inventory():
    print("\n--- Inventory Overview ---")
    
    if not inventory:
        print("The inventory is empty.")
    else:
        for item, details in inventory.items():
            print(f"Item: {item} | Quantity: {details['quantity']} | Price: ₹{details['price']:.2f} | Expiry: {details['expiry'].strftime('%d-%m-%Y')}")


# Main program function for the menu
def main_menu():
    while True:
        print("\n--- Medical Shop Inventory System ---")
        print("1. Add New Item")
        print("2. Delete Item")
        print("3. Search for an Item")
        print("4. View Expired Items")
        print("5. Display Full Inventory")
        print("6. Exit")
        
        choice = input("Select an option (1-6): ").strip()
        
        if choice == '1':
            add_item()
        elif choice == '2':
            delete_item()
        elif choice == '3':
            search_item()
        elif choice == '4':
            expired_items()
        elif choice == '5':
            display_inventory()
        elif choice == '6':
            print("Exiting the system. Have a great day!")
            break
        else:
            print("Invalid choice! Please enter a valid option.")

# Run the main menu if this is the main program
if __name__ == "__main__":
    main_menu()
