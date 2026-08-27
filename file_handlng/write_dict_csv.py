#dictionary to csv file prg
import csv
data_list=[{'course_id':'1','coursename':'betch','stream':'cs'},{'course_id':'2','coursename':'betch','stream':'mechanical'},{'course_id':'3','coursename':'bca','stream':'cs'},{'course_id':'4','coursename':'mtech','stream':'cs'}]
fields=['course_id','coursename','stream']

with open("course.csv","w",newline='') as fspcsv:
    writer = csv.DictWriter(fspcsv,fieldnames=fields)
    writer.writeheader()
    writer.writerows(data_list)    