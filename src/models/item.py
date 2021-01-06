class Item:
    def __init__(self, itemId, name, condition):
        self.itemId= itemId
        self.name= name
        self.condition= condition
    def __str__(self):
        return f"Id:{self.itemId}\tName:{self.name}\tCondition:{self.condition}"

if __name__== "__main__":
    itemOne= Item(0, "book", "used")
    itemTwo= Item(1, "water bottle", "new")
    print(itemOne)
    print(itemTwo)