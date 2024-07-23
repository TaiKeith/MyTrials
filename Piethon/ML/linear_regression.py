# The term regression is used when you try to find the relationship between variables. In ML, and in statistical modeling, that relationship is used to predict the outcome of future events.
# Linear regression uses the relationship between the data-points to draw a straight line through all them. The line can be used to predict future values.

import matplotlib.pyplot as plt
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# Execute a method that returns some important key values of Linear Regression:
slope, intercept, r, p, std_err = stats.linregress(x, y)

# Create a function that uses the slope and intercept values to return a new value. This new value represents where on the y-axis the corresponding x value will be placed:
def myfunc(x):
    return slope * x + intercept

# Run each value of the x array through the function. This will result in a new array with new values for the y-axis:
mymodel = list(map(myfunc, x))

# Draw the original scatter plot
plt.scatter(x, y)

# Draw the line of linear regression
plt.plot(x, mymodel)

# Display the diagram
plt.show()

"""
slope, intercept, r, p, std_err = stats.linregress(x, y)
print(r)

The coefficient of correlation is called 'r'. It ranges from -1 to 1, where 0 means no relationship between values in x-axis and y-axis, and 1 (and -1) means 100% related.
"""
"""
def myfunc(x):
    return slope * x + intercept

We can now use the info gathered to predict future values using the myfunc() function
def myfunc(x):
    return slope * x + intercept

speed = myfunc(10)
print(speed)
"""
