import matplotlib.pyplot as plt
import numpy as np

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

font1 = {'family':'serif', 'color':'blue', 'size':20}
font2 = {'family':'serif', 'color':'darkred', 'size':12}

plt.title("Sports Watch Data", fontdict = font1) # You can use the 'loc' parameter in title() to position the title
plt.xlabel("Average Pulse", fontdict = font2)
plt.ylabel("Calorie Burnage", fontdict = font2)

plt.plot(x, y)
plt.grid()
plt.show()

"""
->plt.grid() is used to plot a grid. You can specify either the x or y axis by plt.grid(axis = 'x')
you can set line properties for the grid by:
    plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
"""
