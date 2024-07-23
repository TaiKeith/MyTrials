emp_details = {
        "Employee":{
            "Dave":{
                "ID":"001",
                "Salary":"20000",
                "Designation":"Team Leader"
                },
            "Ava":{
                "ID":"002",
                "Salary":"15000",
                "Designation":"Associate"
                }
            }
        }
print(emp_details)

# Accessing Items
print(emp_details.keys())
print(emp_details.values())
print(emp_details.get('Employee'))


"""
# Accessing Items
my_dict = {"Dave":"001","Ava":"002","Joe":"003"}
print(my_dict)
print(my_dict.keys())
print(my_dict.values())
print(my_dict.get('Ava'))

for x in my_dict:
    print(x)
for x in my_dict.values():
    print(x)
for x,y in my_dict.items():
    print(x,y)

# Updating
my_dict["Dave"] = "004"
my_dict["Chris"] = "003"
print(my_dict)

# Deleting
my_dict.pop("Ava")
my_dict.popitem()
del my_dict["Dave"]
"""

import pandas as pd
df = pd.DataFrame(emp_details["Employee"])
print(df)
