class Publicdemo:
     def __init__(self,name,city):
         self.name=name
         self.city=city
		  
          
     def print_detail(self):
        print(self.name)
        print(self.city)

obj=Publicdemo("mhk","indore")
obj.print_detail()
print(obj.city)		