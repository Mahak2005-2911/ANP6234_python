from abc import ABC, abstractmethod

class Item_abstract(): 
    @abstractmethod
    def print_item_name(self):
       pass

class Shirt(Item_abstract):
    def show(self):
        print("show of the shirt class")

obj = Item_abstract()
obj.print_item_name()
obj2 = Shirt()
obj2.show()        
      

 