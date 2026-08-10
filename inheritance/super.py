class Person:
    def __init__(self, name, dob, mobile):
        self.name = name
        self.dob = dob
        self.mobile = mobile

    def print_detail(self):
        print(self.name, self.dob, self.mobile)


class Student(Person):
    def __init__(self, classname, subject, course, name, dob, mobile):
        # Call parent constructor
        super().__init__(name, dob, mobile) #can call parent class init method with parentclass name like Person.__init__()
        self.classname = classname
        self.course = course
        self.subject = subject

    def print_student_detail(self):
        print(self.name, self.subject, self.course, self.classname)


# Create object
obj = Student("3rd year", "CS", "BTech_CS", "Mahak", "29-11", 927848778)
obj.print_student_detail()


