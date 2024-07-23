import matplotlib.pyplot as plt
import numpy as np

"""
->With subplot() function you can draw multiple plots in one figure with different titles. For a title to the entire figure, use the "suptitle()" function.
->For subplots we describe (Number of rows, Number of columns, Index of the plot), e.g:
    for 2 subplots side by side:
        plt.subplot(1, 2, 1)
        plt.subplot(1, 2, 2)

    for 2 subplots top and below:
        plt.subplot(2, 1, 1)
        plt.subplot(2, 1, 2)

    for multiple like 6:
        plt.subplot(2, 3, 1)
        plt.subplot(2, 3, 2)
        plt.subplot(2, 3, 3)
        plt.subplot(2, 3, 4)
        plt.subplot(2, 3, 5)
        plt.subplot(2, 3, 6)
"""
# Subplot 1
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 1)
plt.plot(x,y)
plt.grid()
plt.title("JANUARY")

# Subplot 2
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 2)
plt.plot(x,y)
plt.grid()
plt.title("FEBRUARY")

# Subplot 3
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 3)
plt.plot(x,y)
plt.grid()
plt.title("MARCH")

# Subplot 4
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 4)
plt.plot(x,y)
plt.grid()
plt.title("APRIL")

# Subplot 5
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 5)
plt.plot(x,y)
plt.grid()
plt.title("MAY")

# Subplot 6
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 6)
plt.plot(x,y,c='green')
plt.grid()
plt.title("JUNE")

plt.suptitle("FIRST HALF YEAR")
plt.show()
