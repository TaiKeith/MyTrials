import matplotlib.pyplot as plt
import numpy as np

# If we need to plot a line from (1, 3) to (8, 10), we have to pass two arrays [1, 8] and [3, 10] to the plot function.
xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

# To plot only the markers, you can use shortcut string notation parameter 'o', which means 'rings'.
plt.plot(xpoints, ypoints, 'o')
plt.show()
