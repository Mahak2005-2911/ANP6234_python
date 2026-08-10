#parameter in decorator
#exponential

def multi2(fun_obj):
    def myinner(arg):
        return fun_obj(arg)**2 
    return myinner

@multi2
def fun2(x):
    return x  
print(fun2(10))


#multiplication

def multi2(fun_obj):
    def myinner(arg):
        return fun_obj(arg)*2 
    return myinner

@multi2
def fun2(x):
    return x  
print(fun2(20))

#*args ke sth multiple 

def multi_value_deco(fun_obj):
    def myinner(*arg):
        return fun_obj(*arg).upper()
    return myinner

@multi_value_deco
def namelist(*x):
    return "Welcome "+x[0]+x[1]+x[2] 
print(namelist("my name is mahak"))




