def f1(n):
    return lambda a:a*n

mul1 = f1(5)
mul2 = f1(10)
print(mul1(5))
print(mul1(10))
    



    