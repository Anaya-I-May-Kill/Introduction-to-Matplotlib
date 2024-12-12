import matplotlib.pyplot as plt
import numpy as np

x = np.array([0 , 34 , 29 , 72 , 170])
y = np.array([0 , 4 , 13 , 66 , 100])

plt.plot(x , y , marker = "o" , ms = 5 , mec = "r" , linestyle = "dashed")
plt.show()