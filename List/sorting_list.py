# Sorting a list using sort function.
# List_obj.sort():- This will sort the list in ascending order.
# List_obj.sort(reverse=True)
# sorted() this function 


no_list=[10,2,30,4,1,200]
print(no_list)
no_list.sort()
print(no_list)

#To perform reverse sorting we will use the reverse=True

l=[12,2,22,34,9,100]
print(l)
l.sort(reverse=True)
print(l)

#sorted function will arrange the data temporary
l=[12,2,22,34,9,100]
print("Original List", l)
print(sorted(l))
temp_l=sorted(l)
print(temp_l)
print(l)

