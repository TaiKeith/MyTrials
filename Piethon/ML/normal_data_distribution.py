import numpy as np
import matplotlib.pyplot as plt

x = np.random.normal(5.0, 1.0, 100000)  # Mean value is 5.0, Standard Deviation is 1.0

plt.hist(x, 100)  # Plots histogram with 100 bars
plt.show()
