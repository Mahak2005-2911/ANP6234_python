def mydeco(fun_obj):
    def myinner(): 
        return fun_obj()+"$"
    return myinner  

@mydeco
def show():
    return "HELLO WORLD"

print(show())

#decorator ko lower case me krna

def mydeco(fun_obj):
    def myinner(): 
        return fun_obj().lower()
    return myinner  

@mydeco
def show():
    return "HELLO WORLD"

print(show())

	 
#string lower case
@mydeco
def msg():
      return"HELLO IM MAHAK"       
print(msg())


