import matplotlib.pyplot as plt
import numpy as np

"""
xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints)
plt.show()
"""

# If we do not specify the points on the x-axis, they will get the default values 0, 1, 2, 3 (etc., depending on the length of the y-points.
# You can use the keyword argument 'marker' to emphasize each point with a specified marker and 'ms' to set the marker size.
# You can use the keyword argument 'markededgecolor',mec, to set the color of the edge of the marker or 'markerfacecolor',mfc, to set the color inside the edge of the marker.

ypoints = np.array([3, 8, 1, 10, 5, 7])

"""
plt.plot(ypoints, marker = 'o', ms = 10, mfc = 'r')
plt.show()
"""
# You can also use the shortcut string notation parameter to specify the marker.
# This parameter is also called fmt, and is written with the syntax: 'marker|line|color'

#plt.plot(ypoints, 'o:g')
plt.plot(ypoints, 'o-b', ms = 20, mfc = 'r', mec = 'g')
plt.show()

"""
->You can use the keyword argument 'linestyle' or ls, to change the style of the plotted line
->You can use the keyword argument 'color' or c, to change the color of the plotted line
->You can use the keyword argument 'linewidth' or lw, to change the width of the plotted line
plt.plot(xpoints, ypoints, ls = 'solid', c = 'blue', lw = '20.5')
"""
