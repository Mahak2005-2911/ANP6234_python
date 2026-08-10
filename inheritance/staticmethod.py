class Calculate:
    @staticmethod
    def sum(a,b):
        return(a+b)
        
    @staticmethod
    def sub(a,b):
        return(a-b)



print("Sum of 10 & 15 ",Calculate.sum(10,5))       
print("Sum of 10 & 15 ",Calculate.sum(10,5))   

# we can access the static methods with the object of the class

obj = Calculate()
print(obj.sum(20,3))
