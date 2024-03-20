import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,2,100)
y = x**2

toplam_alan = 0
for i in range(len(x)-1):
    alan = (x[i+1]-x[i])*(y[i+1]-y[i])
    toplam_alan += alan
print(f"toplam_alan_Raimann: {toplam_alan}")

plt.plot(x,y,"r*")
plt.show()
