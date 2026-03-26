import re

name = input("What's the name?:")
phone =input("What's the phone number?:")
email = input("What's the email id?:")
if re.match(r"^[0-9]{10}$",phone) and re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',email):
    with open("csvsheet.csv","a") as file:
        file.write(f"{name},{phone},{email}\n")
else:
    print("Check your credentials")

    
