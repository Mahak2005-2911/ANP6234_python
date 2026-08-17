import array as arr_dec
a=arr_dec.array('i',[12,43,433,64,34,44])
print(a)
print(a[3])
print(a[2])

#len function
import array as arr_dec
a=arr_dec.array('i',[12,43,433,64,34,44])
print(a)
print(a[3])
print(a[2])
print(len(a))     #lenght of the function
a.append(29)      #always add element in the last 
#print(a)


a.insert(7,93)
a.insert(1,984)   #insert in a specific indexing
for i in range(0,len(a)):
    print(a[i])


