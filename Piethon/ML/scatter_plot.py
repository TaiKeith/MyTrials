import numpy as np
import matplotlib.pyplot as plt

x = np.random.normal(5.0, 1.0, 1000)  # Mean=5.0, S.D=1.0, value=1000 dots
y = np.random.normal(10.0, 2.0, 1000)  # Mean=10.0, S.D=2.0, value=1000 dots

plt.scatter(x, y)
plt.show()
