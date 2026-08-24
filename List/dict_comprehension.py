#Dictionary comprehension with operation.

my_dict={x:x for x in range (1,50)}
print(my_dict)

my_dict1={x:x*4 for x in range (1,11)}
print(my_dict1)

my_dict1={x:x+4 for x in range (10,11)}
print(my_dict1)

#zip function is used to combine the two list into dict.

empid=[101,102,103,104,105]
empname=["mahak","spna","mahi","akki","bhavna"]
emp_dict={k:v for (k,v) in zip(empid,empname)}
print (emp_dict)

#we have to do create a fruit list and convert it into dictionary.
 
fruit_list=["Apple","Mango","Orange","Banana"]
fruit_dict={x:x for x in (fruit_list)}  
print (fruit_dict)


 
my_dict1={x:x+1 for x in range (0,50)}                 
print(my_dict1)