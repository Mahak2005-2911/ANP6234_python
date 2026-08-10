f=["Apple","banana","mango","banana","orange","apple","papaya"];
print(f)
f.insert(2,"grapes")
print(f)
f.append("cherry")
print(f)
fruits=["chiku","watermelon","lichi"]
f.extend(fruits)
print(f)
f.remove("watermelon")
print(f)
f.remove("banana")#only remove first duplicate value
print(f)
fruits.pop(1)
fruits.pop()
print(fruits)
del fruits[1]
print(fruits)
del fruits
print(fruits)
