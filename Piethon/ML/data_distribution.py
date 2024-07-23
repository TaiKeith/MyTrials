import numpy as np
import matplotlib.pyplot as plt

"""
x = np.random.uniform(0.0, 5.0, 250)  # Create an array containing 250 random floats between 0 and 5

plt.hist(x, 5)  # Plots a histogram with 5 bars
"""

# For a big data set with 100000 random numbers
x = np.random.uniform(0.0, 5.0, 100000)

plt.hist(x, 100)  # Plots a histogram with 100 bars
plt.show()
