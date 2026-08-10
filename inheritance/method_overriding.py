# normal method overriding
class A:
    def show(self):
        print("Show of class A")
        
class B(A):
    def show(self):
        print("Show of class B")


objb = B();
objb.show()        
        
        
# calling the A class through self method.     
class A:
    def show(self):
        print("Show of class A")
        
class B(A):
    def show(self):
        print("Show of class B")
        A.show(self)


objb = B();
objb.show()   


# displayyy method.
class A:
    def show(self):
        print("Show of class A")
        
class B(A):
    def show(self):
        print("Show of class B")
        A.show(self)
        self.display()
        
    def display(self):
        print("display method of the class B")        


objb = B();
objb.show()        
             
                