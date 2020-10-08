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
import pickle

# global vars
catalog = []
last_id = 0
data_file = 'warehouse.data'

# functions

def serialize_catalog():
    global data_file
    writer = open(data_file, 'wb') # wb = create/overwrite the file
    pickle.dump(catalog, writer)
    writer.close()
    print("Data saved!")

def deserialize_catalog():
    global data_file
    global last_id
    try:
        reader = open(data_file,'rb') # rb = read binary
        temp_list = pickle.load(reader)
        
        for item in temp_list:
            catalog.append(item)
        
        last = catalog[-1]
        last_id = last.id + 1
        print("Deserialized " + str(len(catalog)) + " items")
    
    except:
        print("Error, no data loaded")

def register_item():
    global last_id    
    print_header("Register New Item")
    title = input("Please provide title for product: ")
    category = input("Please provide category for product: ")
    try:    
        stock = int(input("Please provide amount of products: "))
        price = float(input("Please provide price per product: "))

        the_item = Item(last_id, title, category, stock, price)
        last_id += 1

        # add the object to the list
        catalog.append(the_item)

        count = len(catalog)
        print("\n\nItem saved, you have " + str(count) + " item(s) in your catalog\n\n")
        serialize_catalog()
    except ValueError:
        print("Error: Invalid Value - Provide a valid number.")
    except: 
        print("Error: Something went wrong. Verify data and try again.")


def display_catalog():  
    print_header("Your Catalog")
    for item in catalog:
        print_item(item)

def display_out_of_stock():
    print_header("Out of Stock")
    for item in catalog:
        if(item.stock == 0):
            print_item(item)

def inventory_value():
    print_header("Inventory Value")
    total = 0.0
    for item in catalog:
        total += item.stock * item.price
    print("Total inventory value: $" + str(total))

def update_price():
    display_catalog()
    item_id = input("Please enter the ID number of the product: ")
    found = False # referred to as a flag
    for item in catalog:
        if(item.id == int(item_id)):
            found = True
            new_price = input("Choose a new price per product: $")
            item.price = float(new_price)
            serialize_catalog()
    if(not found):
        print("Error, invalid ID. Try again.")    

def update_stock():
    display_catalog()
    item_id = input("Please enter the ID number of the product: ")
    found = False # referred to as a flag
    for item in catalog:
        if(item.id == int(item_id)):
            found = True
            stock_change = input("How many would you like to add? Use negative numbers for reduction in stock: ")
            item.stock = item.stock + int(stock_change)
            if(item.stock < 0):
                print("Unable to save changes. Stock can't be a negative number.")
                item.stock = item.stock - int(stock_change)
            else:
                serialize_catalog()
    if(not found):
        print("Error, invalid ID. Try again.")  

def remove_item():
    display_catalog()
    item_id = input("Please enter the ID number of the product: ")
    found = False
    for item in catalog:
        if(item.id == int(item_id)):
            found = True
            confirm = input("Are you sure? If so, type 'Yes': ")
            if(confirm == "Yes"):
                catalog.remove(item)
                print("Item deleted!")
                serialize_catalog()
            else:
                print("Returning to Main Menu...")
    if(not found):
        print("Error, invalid ID try again.")

def display_categories():
    clear()
    print_header("Categories")
    cat_list = []
    i = 1
    for item in catalog:
        if item.category not in cat_list:
            cat_list.append(item.category)
            print("\n" + str(i) + ": " + item.category)
            i = i + 1

def lowest_cost_item():
    clear()
    print_header("Cheapest Item")
    temp = []
    for item in catalog:
        temp.append(item.price)
        temp = sorted(temp)
    for item in catalog:
        if(item.price == temp[0]):
            print_item(item)



def three_expensive_items():
    clear()
    print_header("Three Most Expensive Items")
    temp = sorted(catalog, key=lambda item: item.price)
    print_item(temp[-1])
    print_item(temp[-2])
    print_item(temp[-3])
    

# direct instructions
clear()
deserialize_catalog()
input("Press Enter to continue...")

opc = " "
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
        display_out_of_stock()
    
    elif(opc == "4"):
        inventory_value()

    elif(opc == "5"):
        update_price()
    
    elif(opc == "6"):
        remove_item()

    elif(opc == "7"):
        update_stock()
    
    elif(opc == "8"):
        display_categories()
    
    elif(opc == "9"):
        lowest_cost_item()
    
    elif(opc == "10"):
        three_expensive_items()

    elif(opc == "Knock Knock"):
        print("Who's there?")

    input("\nPress Enter to continue...")
