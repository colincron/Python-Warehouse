import os
import datetime

def print_menu():
    print("-" * 50 + "\n")
    print("      Warehouse Control    " + get_date_time())
    print("-" * 50 + "\n")
    print("[1] Register New Item\n")
    print("[2] Display Catalog\n")
    print("[3] Display Out of Stock Items\n")
    print("[4] Value of Inventory\n")
    print("[5] Update Item Price\n")
    print("[6] Delete an item\n")
    print("[7] Update Item Stock\n")
    print("[8] View Categories\n")
    print("[9] Cheapest Product\n")
    print("[10] 3 most expensive products\n\n")
    print("[x] Close")

def get_date_time():
    now = datetime.datetime.now()
    return now.strftime("%d%b%Y %X")


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_item(item):
    print("\n")
    print("ID:".ljust(20) + str(item.id).rjust(10))
    print("Title:".ljust(20) + item.title.rjust(10))
    print("Category:".ljust(20) + item.category.rjust(10))
    print("Number in stock:".ljust(20) + str(item.stock).rjust(10))
    print("Price per unit:".ljust(20) + str(item.price).rjust(10))
    # STRING.ljust(#) / STRING.rjust(#)

def print_header(text):
    clear()
    print("-" * 30 + "\n")
    print("      " + text + "\n")
    print("-" * 30 + "\n")
