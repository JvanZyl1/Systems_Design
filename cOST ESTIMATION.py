import matplotlib.pyplot as plt
import math
import numpy as np


SN = ['Landsat 6', 'Grace 1', 'ADM-Aeolus', 'TERRA', 'TerraSAR-X']
PM = np.array([398,127,450,1420,130])

'''
plt.bar(SN, PM, color = 'black')
plt.title('First level estimation of wet mass')
plt.xlabel('Spacecraft name')
plt.ylabel('Cost [USSS $ Million]')
plt.show()

x = (398 + 127 + 450 + 1420 + 130)/5

print("The average is", x)
'''

payload = np.array([288, 40, 266, 1155, 349])

m, b = np.polyfit(PM, payload, 1)


plt.plot(PM, payload,'o', color = 'black')
plt.title('First level estimation of cost')
plt.xlabel('Cost [USSS $ Million]')
plt.ylabel('Payload [kg]')
plt.plot(PM, PM*m+b)
plt.show()






