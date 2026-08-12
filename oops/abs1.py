from abc import ABC, abstractmethod

class Item_abstract(ABC): 
    @abstractmethod
    def print_item_name(self):
       pass

class Shirt(Item_abstract):
    def print_item_name(self):
        print("print_item_name of the shirt class")

# obj = Item_abstract()
# obj.print_item_name()
obj2 = Shirt()
obj2.print_item_name()  