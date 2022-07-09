import math
import numpy as np
import matplotlib.pyplot as plt

F = np.array([0.006, 0.105, 0.2, 0.75, 0.85, 1.2, 1.6])
beta = np.array([100, 90, 80, 70, 60, 30, 0])
m, b = np.polyfit(F, beta, 1)


plt.plot(F, beta, 'o', color = 'black')
plt.title('Visbility level changing with beta')
plt.ylabel('Beta[degrees]')
plt.xlabel('Visbility factor')
plt.plot(F, F*m+b)
plt.show()




