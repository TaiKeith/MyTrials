import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 10, 250)  # we use NumPy to randomly generate an array with 250 values, where the values will concentrate around 170, and the standard deviation is 10

plt.hist(x)
plt.show()
