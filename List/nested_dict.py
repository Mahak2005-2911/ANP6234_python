#Nested dictionary

# nested_dict_comp = {key :{key2:val for (key2,val) in range/zip (list1,list2) for key in range/list}

# Example:- 
# person ={pid:1,pname:"mhk dubey","phone":{"home":"02998387489","mobile":9373974879},"address":{"houseno_with_housename":"12/2 vikram nagar","landmark":"near shiv temple ","pincode":452010}}

matrix_dict={x:{k:k for k in range (1,5)} for x in range (0,4)}
print(matrix_dict)

