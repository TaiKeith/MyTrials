import re

Email = input("Enter your email address: ").strip()

if matches:= re.search(r"^([a-zA-Z0-9_]+)(\.[a-zA-Z0-9_]+)@((gmail|hotmail|outlook)\.com)$", Email, re.IGNORECASE):
    print(f"Your username is {(matches.group(1))} & domain is {(matches.group(3))}")
else:
    print("Invalid email address format!")
