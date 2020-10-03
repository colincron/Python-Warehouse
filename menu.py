import os

def print_menu():
    print("-" * 30 + "\n")
    print("      Warehouse Control\n")
    print("-" * 30 + "\n")
    print("[1] Register New Item\n")
    print("[2] Display Catalog\n")
    print("[3] Display Out of Stock Items\n")
    print("[4] Value of Inventory\n\n")
    print("[x] Close")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_item(item):
    print("\n")
    print("ID:              " + str(item.id))
    print("Title:           " + item.title)
    print("Category:        " + item.category)
    print("Number in stock: " + str(item.stock))
    print("Price per unit:  "+ str(item.price))

def print_header(text):
    clear()
    print("-" * 30 + "\n")
    print("      " + text + "\n")
    print("-" * 30 + "\n")
