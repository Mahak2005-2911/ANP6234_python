import re

text = input("Enter any sentence:-")

search_str = input("Now enter the word you want to search:-")

result = re.search(search_str,text)
if result:
    
    print("Given text is found")