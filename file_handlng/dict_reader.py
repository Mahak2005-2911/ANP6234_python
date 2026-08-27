import csv 

data_list=[]

with open ('student.csv','r') as fspcsv:
    csv_reader=csv.DictReader(fspcsv)
  
    for row in csv_reader:
        data_list.append(row)

for item in data_list:

    print(item)		