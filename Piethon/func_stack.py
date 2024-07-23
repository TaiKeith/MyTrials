def func_stack():
    stack = ["car", "candy", "fruit", "bike"]
    results = (stack.pop(1) if stack.pop(0) != "candy" else stack.pop())
    return results
    
print(func_stack())

"""
Here is the explanation
The interpreter does what he sees by order
First :
stack.pop(1) is executed a first time :
So "candy" is poped

Second:
Then the if condition is checked
That is : stack.pop(0)
which is equal to : "car"

As you need to remember that pop returns
the value removed and takes a position
as parameter

Third:
As the condition is filled , then again
stack.pop(1) is executed and
as "car" and "candy" have already been removed
before the last stack.pop(1) is executed,
stack:= ["fruit", "bike"]

So, you keep "fruit"
"""
