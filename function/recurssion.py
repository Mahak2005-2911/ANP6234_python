def print_no(n):
    if n == 0:
        return
    print(n)
    print_no(n-1)
    
print_no(10)