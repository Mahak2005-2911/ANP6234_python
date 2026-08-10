class Items:
    types_of_items="cloths"
    
    
print(Items.types_of_items)
obj1=Items()  
obj2=Items()      
print(obj1.types_of_items)
print(obj2.types_of_items)
Items.types_of_items="cloths and cosmetics "
print(Items.types_of_items)
print(obj1.types_of_items)
print(obj2.types_of_items)
obj1.types_of_items="food items"
#when we update the value of the static variable by obj of the class 
#it created a member vaRIABLE for that object,and objectwill always has access to the variable ,other object will access the static variable only.
print("static variable",Items.types_of_items)
print("using obj1",obj1.types_of_items)  
print("using obj2",obj2.types_of_items)