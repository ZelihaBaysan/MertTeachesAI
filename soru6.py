import numpy as np
import matplotlib.pyplot as plt


m = 1000

x_rand = np.random.rand(m) * 2*np.pi
y_rand = np.random.rand(m) * 2

x = np.linspace(0, 2*np.pi, m) 
y = np.cos(x)

under_filter = y_rand <= np.cos(x_rand) 


plt.plot(x, y, "r-")
plt.scatter(x_rand, y_rand, s=1)
plt.scatter(x_rand[under_filter], y_rand[under_filter], s=1) 
plt.show()



