import numpy as np
import matplotlib.pyplot as plt

m = 10000
x_rand = np.random.rand(m) * 2
y_rand = np.random.rand(m) * 4
x = np.linspace(0, 3, m)
y = x**2
under_filter = (y_rand < x_rand**2)
under_dot = len(x_rand[under_filter])
area = (under_dot * 8) / m

plt.plot(x, y, "r-")
plt.scatter(x_rand, y_rand, s=1)
plt.scatter(x_rand[under_filter], y_rand[under_filter], s=1)
plt.axvline(x=2, color="b", linestyle="--")
plt.axhline(y=4, color="r", linestyle="--")
plt.show()

print("analitik area: ", 8 / 3)
print(f"under area: {area}")
