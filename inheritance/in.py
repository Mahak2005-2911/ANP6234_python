class Person:
    def printdata(self):
        print("hello")


class Stu(Person):
    def m1(self):
        print("m1 of student class")
        
s = Stu()
s.printdata()
s.m1()        