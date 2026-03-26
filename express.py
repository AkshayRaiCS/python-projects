import re
def user_name(name):
    if re.match(r"^\w{3,16}$",name):
        return True
    else:
        return False
print(user_name("cool_user123"))
print(user_name("ab"))
print(user_name("no spaces"))