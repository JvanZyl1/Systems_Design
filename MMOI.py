# Moments of Inertia program: CASE 1

import math
import matplotlib.pyplot as plt
import numpy as np


mlow = 1380.78 + 250 + 126.57
mhigh = 2082.72 + 450 + 171.63

Ix = []
Iy = []
Iz = []
m = np.arange(mlow,mhigh, 0.1)
n = 0

for i in np.arange(mlow, mhigh, 0.1):
    n = (1/12)*i*(2.5**2 + 0.75**2) + 2((1/12)*11.43*(61**2))+11.43*(0.25**2 + 0.75**2)
    np.append(Ix,n)

for j in np.arange(mlow, mhigh, 0.1):
    n = (1/12) * j *(1.5**2 + 2.5**2) + 2((1/12)*11.43*2.5**2)+11.43*(3**2 + 0.75**2)
    Iy.append(n)

plt.plot(Ix, m,'o', color = 'black')
plt.title('How the Ix moment changes with respect to mass')
plt.xlabel('Mass [kg]')
plt.ylabel('I_x [kg*m^2]')
plt.show()

plt.plot(Iy, m,'o', color = 'black')
plt.title('How the Iy moment changes with respect to mass')
plt.xlabel('Mass [kg]')
plt.ylabel('I_y [kg*m^2]')
plt.show()

for k in np.arange(mlow, mhigh, 0.1):
    o = (1/12)*k*(1.5**2 + 2.5**2) + 2(1/12 * 11.43 * (61**2 + 2.5**2)**0.5)+ 11.43*(3**2 + 0.25**2)
    Iz.append(o)

plt.plot(Iz, m,'o', color = 'black')
plt.title('How the Iz moment changes with respect to mass')
plt.xlabel('Mass [kg]')
plt.ylabel('I_z [kg*m^2]')
plt.show()


