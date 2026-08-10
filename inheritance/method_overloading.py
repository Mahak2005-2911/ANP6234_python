# error aayegi bcz python do not support overloading
def sum(a,b):
   print(a+b)
  
def sum(a,b,c):
   print(a+b+c)

sum(10,5,5)
sum(10,5)  


#through args it will give the output 
def sum(a,b):
   print(a+b)
  
def sum(a,b,c):
   print(a+b+c)
   
def sum (*args):
   pass    

sum(10,5)
sum(10,5,5)  