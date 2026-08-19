# reverse() is used to reverse a list .but in this we create a logic to reverse the list.
l=[12,2,22,34,9,100]
print("Original List:-",l)
print(sorted(l))
length=len(l)
for i in range(0,length//2):
    t=l[i]
    l[i]=l[length-1]
    l[length-i-1]=t
print(l)    
    