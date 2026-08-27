import csv

class Crud_csv:

    def __init__(self, colname):
        with open("student.csv", "w", newline='') as fspcsv:
            csvwrite_obj = csv.writer(fspcsv)
            csvwrite_obj.writerow(colname)

    def add_item_csv(self, data):
        with open("student.csv", "a", newline='') as fspcsv:
            csvwrite_obj = csv.writer(fspcsv)
            csvwrite_obj.writerow(data)

    def print_item_csv(self):
        with open("student.csv", "r", newline='') as fspcsv:
            csvreader = csv.reader(fspcsv)
            col_names = next(csvreader)
            print(col_names)

            for csvrow in csvreader:
                print(csvrow)


obj = Crud_csv(['roll_no', 'sname', 'sdob', 'sadd_date', 'classname'])

choice = 'y'

while choice == 'y' or choice == 'Y':
    datalist = []

    rollno = input("Enter rollno: ")
    sname = input("Enter student name: ")
    sdob = input("Enter student date of birth: ")
    sadd_date = input("Enter student admission date: ")
    classname = input("Enter student class name: ")

    datalist.append(rollno)
    datalist.append(sname)
    datalist.append(sdob)
    datalist.append(sadd_date)
    datalist.append(classname)

    obj.add_item_csv(datalist)

    choice = input("Want to add more Y/N: ")

obj.print_item_csv()