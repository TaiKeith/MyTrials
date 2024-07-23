class User:
    id = 47
    name = ["Keith", "Steve", "Admin", "Juma"]
    _password = (3.142, "Admin123")

    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name


name = input("Enter your name: ")
password = float(input("Enter your password: "))

if name in User.name and password in User._password:
    print("Successfully logged in")
else:
    print("Intruder!")
