class Op_overload_exp2:
    def __init__(self,status):
        self.status=status
        
    def __and__(self,obj2):
        return self.status and obj2.status

t1 =  Op_overload_exp2(True)
t2 =  Op_overload_exp2(False)
t3 =  Op_overload_exp2(True)
        
print (t1 & t2)
print (t1 & t3)                