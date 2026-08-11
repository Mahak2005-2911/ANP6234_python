class Student:
    def __init__(self):
        self.__sname=''
        self.__mobile=0
        self.__classname=''
        self.__subject=''
        
        
    def get_sname(self):
       return self.__sname
    def set_sname(self,name):
       self.__sname=name

    def get_mobile(self):
       return self.__mobile
    def set_mobile(self,mobile):
       self.__mobile=mobile
        
    def get_classname(self):
       return self.__classname
    def set_classname(self,classname):
       self.__classname=classname
       
       
    def get_subject(self):
       return self.__subject
    def set_subject(self,subject):
        self.__subject=subject        
        
        
objs= Student()

#we write class for database operation
#we need to store,update,delete,fetch data for student table.
#i can set all value to an object and pass tht object to the method and by calling getter method i db ope class we get all values and queries will be executed.
objs.set_classname("bca")
objs.set_sname("mhk")
objs.set_mobile(9876543234)
objs.set_subject("computer application")

print(objs.get_sname())
print(objs.get_mobile())
print(objs.get_classname())
print(objs.get_subject())

