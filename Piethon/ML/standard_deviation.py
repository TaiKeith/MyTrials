import numpy as np

speed = [32,111,138,28,59,77,97]

# Standard Deviation
"""
Squareroot of Variance
"""

x = np.std(speed)

# Variance 
"""
1. Find the mean
2. For each value find the difference rfm the mean
3. Forr each difference find the square value
4. Variance is average of the squared differences
"""

y = np.var(speed)

print("Standard deviation is:",x)
print("Variance is:",y)
