def my_gen():
    yield 'a'
    yield 'b'
    yield 120
    yield 37.5
    yield True
    yield 'f'
    
for i in my_gen():
    print(i)
    
def loop_gen(x):
    i=1
    while i<=x:
        return i
        i+=1
        
n = loop_gen(5)
print(n)
n = loop_gen(5)
print(n)
n = loop_gen(5)
print(n)


        
#for n in loop_gen(5):
#    print(n)
 
 
def gen_no_sqrt(n):
    for k in range(n):
        yield k*k
         
sqrt = gen_no_sqrt(1000000)
print(next(sqrt))
print(next(sqrt))
print(next(sqrt))
