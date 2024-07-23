import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]: # Slice
    print("Hello, my name is", arg)
