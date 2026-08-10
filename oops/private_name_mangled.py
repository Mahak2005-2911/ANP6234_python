class Emp:
    def __init__(self,name,dob,salary):
        self.__name=name
        self.__dob=dob
        self.__salary=salary
        
    def print_details(self):
        print(self.__name)
        print(self.__dob)
         
e=Emp("mhk","29-11","35000")
print(e.print_details())   
print(dir(e))
print(e._Emp__salary)
        
    