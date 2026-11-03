import re

text = input("Enter any sentence:-")

search_str = input("Now enter the word you want to search:-")

esc_text = re.escape(text)
esc_s_str = re.escape(search_str)
result = re.search(esc_s_str,esc_text,flags=re.I)

if result:
    print("Given text is found")
    print(result.start())
    print(result.end())