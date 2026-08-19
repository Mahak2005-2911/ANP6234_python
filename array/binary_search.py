import array as arr_dec
a = arr_dec.array('i',[10,20,30,34,44,56,78,98]) #binary search is only working on sorted array

low=0
high=len(a)-1

item =int(input("Enter no to be searched:-"))
while low<high:
    mid=int((low+high)/2)
    if item==a[mid]:
        print("Item Found At Index",mid)
        break
    elif item<a[mid]:
        high=mid-1
    elif item>a[mid]:
        low=mid+1
		 
if low>high:
        print("index not found")		 
		 	 