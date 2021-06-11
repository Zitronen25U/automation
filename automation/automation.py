from os import read
import re

        
phone_numbers = [] 

phone_number_search = r".*?(\(?\d{3}\D{0,3}\d{3}\D{0,3}\d{4}).*?"

with open("potential-contacts.txt", "r") as file: 
    for i in file: 
        result = re.search(phone_number_search, i)
        phone_numbers.append(result.group(1))
print(phone_numbers)

