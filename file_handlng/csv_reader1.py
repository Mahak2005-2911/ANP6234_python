import csv 
col_names =[]
data=[]

with open ('student.csv','r') as fspcsv:
    csvreader=csv.reader(fspcsv)
    col_names=next(csvreader) # we read first line  and pass it to colname list 
    for csvrow in csvreader:
        data.append(csvrow)
# print(col_names)
# print(data)

print("".join(col_names))
for row in data :
        # for v in row:  
    print("".join(row))
            