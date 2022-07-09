import matplotlib.pyplot as plt
import numpy as np
import math

LM = np.array([2750, 500, 1360, 1360, 4863, 1230])
PM = np.array([120, 34, 116, 266, 326,78])
m, b = np.polyfit(LM, PM, 1)


plt.plot(LM, PM,'o', color = 'black')
plt.title('Vehicle level sizing of propellant mass')
plt.xlabel('Launch Mass [kg]')
plt.ylabel('Propellant Mass [kg]')
plt.plot(LM, LM*m+b)
plt.show()
