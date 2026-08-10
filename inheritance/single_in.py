class Person:
    def __init__(self, fname, lname, mobile):
        self.fname = fname
        self.lname = lname
        self.mobile = mobile

    def printdetail(self):
        print(self.fname)
        print(self.lname)
        print(self.mobile)

class Student(Person):
    pass

objstu = Student("mhk", "dubey", 9367678776)
objstu.printdetail()
    