import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])


# If you want the bars to be displayed horizontally instead of vertically, use the barh() function ->plt.barh(x, y)
# The bar() and barh() take the keyword argument color to set the color of the bars -> plt.bar(x,y,color="green")
# The bar() takes the keyword argument width to set the width of the bars -> plt.bar(x,y, width=0.5)
# The barh() takes the keyword argument height to set the height of the bars -> plt.barh(x,y, height=0.5)

plt.bar(x, y)
plt.show()
