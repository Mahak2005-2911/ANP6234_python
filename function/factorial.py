# Factorial of a number
# factorial of a numberby multiply.......screen shot
def fact_rec(n):
    if n==1: 
        return 1
    else:
        r = n*fact_rec(n-1)
        return r		
		

no = int(input("Enter any no -ve integer no:-"))
if  (no<0):
    sys.exit("-ve no. doesn't have factorial") 
elif no==0:
      print ("Factorial is 1 of 0")

elif no==1:
      print("Factorial is the 1 of 1")
	  
else :

	 result = fact_rec(no)
	 print("Factorial of",no,result)
	  
	