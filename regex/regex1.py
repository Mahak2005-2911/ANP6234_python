import re

string = "This is lion 555-1234"
# matching_result = re.search(r'\d{3}',string)
# matching_result = re.search(r'\d{3}-\d{4}',string)
matching_result = re.search(r'\d{4}',string)

if matching_result:
        
    print("record found")