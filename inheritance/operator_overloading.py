# steps to perform the operator overloading 
# First declare the magic operator



# print (10+3)
# print ("hello"+"world") 

#__add__ method

class Op_overload_exp1:
    def __init__(self,no):
        self.no=no
    def __add__(self,obj2):  
        return self.no+obj2.no
        
obj1=Op_overload_exp1(10)
obj2=Op_overload_exp1(100)     

print (obj1+obj2)
print(Op_overload_exp1.__add__(obj1,obj2))
print(obj1.__add__(obj2))
