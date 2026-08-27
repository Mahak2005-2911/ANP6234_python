#fsp=file string pointer
fsp =open("students.txt.txt");  #absolute 
print(fsp.read());

with open("students.txt.txt", "rt") as f:
    print(f.readline())
    print(f.readline())
    print(f.readline())

with open("students.txt.txt", "rt") as f2:
    for x in f2:
        print(x)        