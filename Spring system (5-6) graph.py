import math
import numpy as np
import matplotlib.pyplot as plt

#Constants
m_tank = 73.65

k_a = 46646367.72 # of the propellant tank
omega_n = (k_a/m_tank)**0.5
F_0 = 9.5 * 9.80665
f_0 = F_0/m_tank
x_0 = F_0/k_a


t = np.arange(0.001, 0.5, 0.0001)

x_max = []
omega_f = np.arange(0,200,1)


for h in omega_f:
    f = h*2*3.14159
    j = 0
    for i in t:
        x_p = (f_0/(omega_n**2-f**2))*math.sin(f*i)
        if x_p > j:
            j = x_p
    x_max.append(j)

plt.plot(omega_f, x_max)
plt.title('f [Hz] vs x,p_max [m]')
plt.ylabel('x,p_max [m]')
plt.xlabel('f [Hz]')
plt.grid(True)
plt.show()
