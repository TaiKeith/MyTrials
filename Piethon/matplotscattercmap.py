# You can specify the colormap with the keyword argument cmap with the value of the colormap, in this case 'viridis' which is one of the built-in colormaps available in Matplotlib.
# In addition you have to create an array with values (from 0 to 100), one value for each point in the scatter plot

import matplotlib.pyplot as plt
import numpy as np

"""
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, c=colors, cmap='viridis')

# You can include the colormap in the drawing by including the plt.colorbar() statement
plt.colorbar()

plt.show()
"""

# You can change the size of the dots with the s argument.
# -> Just like colors, make sure the array for sizes has the same length as the arrays for the x- and y-axis
# You can adjust the transparency of the dots with the 'alpha' argument

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

plt.scatter(x, y, s=sizes, alpha=0.5)

plt.show()
