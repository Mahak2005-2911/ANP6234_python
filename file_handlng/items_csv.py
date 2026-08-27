#item.csv in which item details will be stored.
#name,price,dom,doe,brandname
import csv

colname=['name','price','dom','doe','brandname']
items=[['pink color shirt','600','12-2-2026','null','nike'],['black color shirt','500','17-03-2026','null','levis'],['red lower','600','18-1-2026','null','lya'],['shirt','600','12-2-2022','null','nike'],['orange color shirt','600','12-2-2026','null','nike']]

with open('item_detail.csv','w',newline='')as fspcsv:
    csvwrite_obj=csv.writer(fspcsv)
    csvwrite_obj.writerow(colname)
    for item in items:
        csvwrite_obj.writerow(item)