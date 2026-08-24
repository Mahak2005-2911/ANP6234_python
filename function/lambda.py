#lambda
s = lambda a:a*5
print(s(10))


s = lambda a:a**2
print(s(10))

s = lambda a:a
print(s(-5)*(-5))

max2 = lambda a,b:a if a>b else b
print(max(10,5))


max3 =lambda a,b,c:a if a>b>c else c
print(max3(2,145,82))