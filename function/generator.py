def mygen():
    yield 'a'
    yield 'b'
    yield 'c'
    yield 'd'
    yield 'e'
	
for v in mygen():
    print (v)	   
	   
       
def mygen():
    yield 'a'
    yield '1'
    yield 'True'
    yield 'd'
    yield '37.4'
	
for v in mygen():
    print (v)	   
	          