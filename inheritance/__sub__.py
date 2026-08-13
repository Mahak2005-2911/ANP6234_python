class Op_overload_exp1:
    def __init__(self,no):
        self.no=no
        
    def __sub__(self,obj2):  
        return self.no-obj2.no     #substract method used to subs the num
        
    def __gt__(self,obj2):  
         return self.no>obj2.no    #gt method find the greater one
        
        
obj1=Op_overload_exp1(10)
obj2=Op_overload_exp1(100)     


print (obj1-obj2)
print(Op_overload_exp1.__sub__(obj1,obj2))
print(obj1.__sub__(obj2))


if obj1>obj2:
    print("Obj1 is greater" )
else:
    print("Obj1 is greater") 
