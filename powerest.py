import matplotlib.pyplot as plt
import numpy as np
import math

LM = np.array([2750 , 500, 1360, 4863, 1230])
Pnom = np.array([1295, 620, 1400, 2530, 800])
m, b = np.polyfit(LM, Pnom, 1)


plt.plot(LM, Pnom,'o', color = 'black')
plt.title('First level estimation of nominal power')
plt.xlabel('Launch mass [kg]')
plt.ylabel('Nominal power [W]')
plt.plot(LM, LM*m+b)
plt.show()
