with open ("students.txt.txt","rt") as fsp:
   total_line = sum(1 for line in fsp)
   
print(total_line)