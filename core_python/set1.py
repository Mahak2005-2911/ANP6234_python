s={"anshu","niku","anu","raja","ram","harshu"}
print(s)
s.add("mhk")
s.add("mahi")
print(s)
s.remove("mhk")
print(s)        #element milaa toh remove kar dega otherwise error dega 
s.discard("mahak")#mila toh bhi thik he nhi toh ignore krdega
listset=["pari","puja","babu"]
s.update(listset)
print(s)