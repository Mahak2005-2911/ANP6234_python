class Animal:
    def print_animal(self):
        print("I am Animal")
        
        
class Mammal(Animal):
    def birth_type(self):
        print("it give birth to the child ")


class Birds(Animal):
    def lay_eggs(self):
        print("It gives the eggs and child came out after some time")


class Platypus(Birds,Mammal):
    pass 


obj =Platypus()

obj.print_animal()
obj.birth_type()
obj.lay_eggs()    