import numpy as np
from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

#mean = sum(speed)/len(speed)
#print(mean)

x = np.mean(speed)
y = np.median(speed)

z = stats.mode(speed)

print("Mean is:", x)
print("Median is:", y)
print("Mode is:", z)
