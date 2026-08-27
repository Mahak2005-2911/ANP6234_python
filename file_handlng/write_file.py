# fsp = open("flowers.txt","w")
# fsp.write("tulip")
# fsp.close()


# fsp = open("flowers.txt","rt")
# print(fsp.read())
# fsp.close()

fsp = open("flowers.txt","w")
fsp.write("sunflower,\n jasmin,\n daisy")
fsp.close()


fsp = open("flowers.txt","rt")
print(fsp.read())
fsp.close()

