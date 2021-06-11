from os import read, write
import re

        
phone_numbers = [] 

email_address = []

phone_number_search = r".*?(\(?\d{3}\D{0,3}\d{3}\D{0,3}\d{4}).*?"
email_search = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"


with open("potential-contacts.txt", "r") as file: 
    for i in file: 
        phone_result = re.search(phone_number_search, i)
        phone_numbers.append(phone_result.group(1))

        email_result = re.search(email_search, i)
        email_address.append(email_result)


with open("phone_output.txt", "w") as f:
    for i in phone_numbers:
        print(f, i)
        f.close()

with open("email_output.txt", "w") as g:
    for i in email_address:
        print(g, i)
        g.close()
