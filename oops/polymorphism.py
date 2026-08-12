class Vehicle:
    def move(self):
        print("Vehicle moves")
        
class Boat:
    def move(self):
        print("Boat sail")
        
        
class Plane:
    def move(self):
        print("Plane fly")

objp=Plane()
objp.move()

        
objp=Boat()
objp.move()


----------------------------------------------------------------


#polymorphic loop

class Vehicle:
    def move(self):
        print("Vehicle moves")
        
class Boat:
    def move(self):
        print("Boat sail")
        
        
class Plane:
    def move(self):
        print("Plane fly")

objs = [Plane(),Boat()]
for x in objs:
 
  x.move()