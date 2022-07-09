import matplotlib.pyplot as plt
import numpy as np
import math

LM = np.array([2750, 500, 1360, 4863, 1230])
PM = np.array([288, 40, 266, 1155, 349])
m, b = np.polyfit(LM, PM, 1)


plt.plot(LM, PM,'o', color = 'black')
plt.title('First level estimation of wet mass')
plt.xlabel('LM')
plt.ylabel('PM')
plt.plot(LM, LM*m+b)
plt.show()


av = (2750+500+1360+4863+1230)/5

print(av)
