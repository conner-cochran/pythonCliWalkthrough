"""
Work wants an inventory app that:
    stores data into a file
    uses the command line to list/add/update/delete:
        "items" they have:
            id
            name
            cond
"""

nextId= 0
items= [1, 2, 3]
# TODO:
# Make a menu printout showing options
def menu():
    print("""
    1. List All Items
    2. Add New Item
    3. Update Existing Item
    4. Delete Item (By Item ID)
    5. Exit
    """)

# Lists All Items
def listItems():
    for item in items:
        print(item)
    pass
    print("in list item function")

# Add New Item
def newItem():
    global nextId
    name= input("Name: ")
    cond= input("Condition: ")
    itemId= nextId
    nextId+= 1

# Update existing Item
def updateExisting(itemId):
    pass

# Delete Item (By Item ID)
def deleteItem(itemId):
    pass

# Make the menu questions that grab the data
while True:
    menu()
    try:
        choice= int(input("> "))
    except Exception:
        input("Invalid Input, give a number\n(Press enter to try again)")
        continue

    if choice== 1:
        listItems()
    elif choice== 2:
        newItem()
    elif choice== 3:
        pass
    elif choice== 4:
        pass
    # Exit
    elif choice== 5:
        exit()
    else:
        input("Invalid Input, give a number\n(Press enter to try again)")


# Make the file saving stuff



