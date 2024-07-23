"""
name = input("What is your name?\n").strip()
if "," in name:
    last, first = name.split(", ")
    name = f"{first} {last}"
print(f"Hello, {name}")
"""
import re

name = input("What is your name?\n").strip()
if matches := re.search(r"^(.+), *(.+$)", name):
    name = matches.group(2) + " " + matches.group(1)
print(f"Hello, {name}")
