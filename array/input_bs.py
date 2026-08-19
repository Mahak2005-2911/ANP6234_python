import array as arr_dec

n = int(input("Enter number of elements: "))

no_array = arr_dec.array('i')

for i in range(n):
    value = int(input("Enter element: "))
    no_array.append(value)

length = len(no_array)

for i in range(0, length):
    for k in range(0, length - 1):
        if no_array[k] > no_array[k + 1]:
            t = no_array[k]
            no_array[k] = no_array[k + 1]
            no_array[k + 1] = t

print("Sorted Array:")

for i in range(0, length):
    print(no_array[i])    