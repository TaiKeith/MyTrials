import numpy as np

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

# What is the 75. percentile? The answer is 43, meaning that 75% of the people are 43 or younger.
x = np.percentile(ages, 75)
y = np.percentile(ages, 90)

print("The 75. percentile is:", x)
print("The 90. percentile is:", y)
