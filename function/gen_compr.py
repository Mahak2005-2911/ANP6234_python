list_compre = [n*n for n in range(1,10)]
print(list_compre)

gen_list_compre = (n*n for n in range(1,10))

print(gen_list_compre)
print(list(gen_list_compre))

def my_gen2():
    yield 1
    yield 2
    yield 3

print(list(my_gen2()))
print(list(my_gen2()))

n= my_gen2()
print(next(n))