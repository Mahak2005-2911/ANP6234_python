# 12  2  1  22  45  55  90  82    element of array 
 # 0  1  2   3   4  5    6   7       indexing
 
 # input from user:-user entered 55

# 0 index we will check a[0]=55 if true we will print element found else we will move to thr another index.
 # 1 we will check a[1]==55
 # 2 a[2]==55
 # 3 a[3]==55
 # 4 a[4]==55
 # 5 a[5]==55 
 
import array as arr_dec
a = arr_dec.array('i',[12,22,234,33,345,56,1,3,2])

no = int(input("Enter any no."))
i=0
while i<len(a):
   if a[i]==no:
        print("Element found at location",i)
        break
        i+=1

if i==len(a):
        print ("Element not found")    
        
        
#because if element found at location n-1 to n-10 in an array of 1000 elements.       order of searching 0(n) it is always        