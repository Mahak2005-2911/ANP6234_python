import array as arr_dec

no_array = arr_dec.array('i', [12, 22, 234, 33, 345, 56, 1, 3, 2])
length = len(no_array)
for i in range(0,length):
   for k in range(0,length-1):  #0 1 2 3
        if (no_array[k]>no_array[k+1]):
            t= no_array[k]
            no_array[k]=no_array[k+1]
            no_array[k+1]=t


for i in range(0,length):	
    print (no_array[i])
    
