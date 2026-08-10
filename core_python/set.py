#normal set
fruiset={"apple","mango","banana",1,True,False,0,}
print(fruiset)

#remove set
city=(("indore","ujjain","dewas"))
print(city)
citylist=["indore","ujjain","dewas","rajgad","bilaspur","rajgad","bilaspur"]
print("List of cities is",citylist)
print("After removing ")
cityset=set(citylist)
print(cityset)

#with for loop and not in in operator. not in me jaha element exist nhi hota toh true deta he,or in me exist krta to true deta h.
for x in cityset:
    print(x)
print("indore"in cityset)
print("indore" not in cityset)
print("delhi"not in cityset)
      