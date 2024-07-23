import re

email = input("Please enter your email address\n").strip()

if re.search(r"^(\w|\.)+@\w+\.com$", email, re.IGNORECASE):# \w -> word xters[a-zA-Z]
    print("Valid")
else:
    print("Invalid")
