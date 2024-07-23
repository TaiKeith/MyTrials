class User:
    id = 47
    name = "Keith"
    _password = 3.142

    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name

"""
ID = input("Enter your ID: ")
if ID != User.id:
    print("Unauthorized!")
    exit()
"""
"""print(User.__dict__)
print(User._password)"""

name = input("Enter your name: ")
password = float(input("Enter your password: "))

if name == User.name and password == User._password:
    print("Successfully logged in")
else:
    print("Intruder!")
