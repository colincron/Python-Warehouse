"""
Program: Warehouse Control
Author: Colin Cron
Functionality: 
    - Register Items
        - id (auto generated): int
        - title: str
        - category: str
        - stock: int
        - price: float

"""

# imports
from menu import print_menu, clear, print_item, print_header
from item import Item

# global vars
catalog = []


# functions
def register_item():
    print_header("Register New Item")
    title = input("Please provide title for product: ")
    category = input("Please provide category for product: ")
    stock = int(input("Please provide amount of product: "))
    price = float(input("Please provide price per product: "))

    the_item = Item(1, title, category, stock, price)

    # add the object to the list
    catalog.append(the_item)

    count = len(catalog)
    print("\n\nItem saved, you have " + str(count) + " item(s) in your catalog\n\n")

def display_catalog():  
    print_header("Your Catalog")
    for item in catalog:
        print_item(item)

def out_of_stock():
    print_header("Out of Stock")
    for item in catalog:
        if(item.stock == 0):
            print_item(item)

def inventory_value():
    print_header("Inventory Value")
    cost = 0
    for item in catalog:
        cost += item.stock * item.price
    print(cost)


# direct instructions
opc = ""
while(opc != 'x'):
    clear()
    print_menu()
    
    opc = input("\n\nPlease select an option: ")

    if(opc == "1"):
        register_item()

    elif(opc == "2"):
        # create function, call, travel list and display title.title
        display_catalog()
    
    elif(opc == "3"):
        out_of_stock()
    
    elif(opc == "4"):
        inventory_value()

    elif(opc == "Knock Knock"):
        print("Who's there?")

    input("\nPress enter to continue...")
