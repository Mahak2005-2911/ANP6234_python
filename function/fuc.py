def mess():
    print("Hello bro how are you")
mess()    

def interest(p,r,t):
    si=(p*r*t)/100
    return si
print (interest(1000,10,5))   
print (interest(1070,6,5))
print (interest(7000,1,5))      
print (interest(2380,9,5))   

#write a program to calculate the SI take principal,rate of interest and time .(Time can be in days,month,or year)

# def interest(P, R, T, unit):
    # if unit == "days":
        # T = T / 365
    # elif unit == "months":
        # T = T / 12

    # return (P * R * T) / 100

# P = float(input("Principal: "))
# R = float(input("Rate: "))
# T = float(input("Time: "))
# unit = input("Unit (days/months/years): ")

# SI = interest(P, R, T, unit)
# print("Simple Interest =", SI)



#29-july (*arbitiary opretor)

def mycolur_listfun(*colorlist):
    print(colorlist)
    print(colorlist[2])
    
    mycolur_listfun("red","green","blue","orange")
    
def s_data(st1,*sttuple):
    print(st1)
    print(sttuple)
s_data("anil","sunil","jay","vinod")
 

#print maximum no out of n number passed to any function using args

# def maximum(*args):
    # max_num = max(args)  
    # print("Maximum number is:", max_num)

# print_maximum("534,28,44,26,")



#dictonary in function

def mydict(**dict_data):
    print(dict_data)
    mydict(fname="mhk",lname="dubey",dob="29-11-05",age="21")