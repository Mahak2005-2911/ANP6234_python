class Op3:
    def __init__(self,v1,v2):
        self.v1=v1
        self.v2=v2
		
		
    def __add__(self,obj2):
	    return self.v1+obj2.v1,self.v2+obj2.v2
		
		
t1 = Op3(10,4)
t2 = Op3(20,4)

print(t1+t2)		
		