import requests

"""
r = requests.get("https://www.kabarak.ac.ke")

#print(r.status_code)
print(r.headers)
"""

"""
# payload = {"page": 2, "count": 25}
# r = requests.get("https://httpbin.org/get", params=payload)

payload = {"username": "tai", "password": "testing"}
r = requests.post("https://httpbin.org/post", data=payload)

r_dict = r.json()
print(r_dict["form"])
# print(r.text) --> print(r.json())
"""

"""
r = requests.get("https://httpbin.org/basic-auth/tai/testing", auth=("tai", "testing"))

print(r.text)
"""

"""
r = requests.get("https://httpbin.org/delay/3", timeout=3)

print(r)
"""

# r.text -> print the content of the result in unicode

# to download image from web
r = requests.get("https://imgs.xkcd.com/comics/python.png")
with open("comic.png", "wb") as f:
    f.write(r.content)
