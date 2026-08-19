# Remove duplicates form list
# By converting a list in set
#dict_obj.formkeys(list_name)
# my_list_unique = list(dict.fromkeys(l))using this function we remove the duplicacy elements.

l=[10,20,30,4,5,6,10,20,30,4,5,6]
print("Original List:-",l)
my_list_unique = list(dict.fromkeys(l))
print("After removing the elements:-",my_list_unique)

#Creating function that will return a list with 
marks =[33,44,55,66,67,88,99,96,23,30]
#defining our filter function
def my_marks_filter(m):
    if m<50:
         return m
marks_list_below_50 = list(filter(my_marks_filter,marks))
print("The marks of the Students:-",marks )
print( "The marks below 50 is the following:-",marks_list_below_50)    

