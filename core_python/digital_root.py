

num = int(input("Enter a number: "))

while num > 9:   # keep looping until num is a single digit
    result = 0
    while num > 0:
        x = num % 10
        result = result + x
        num = num // 10
    num = result

print("Digital root:", num)
