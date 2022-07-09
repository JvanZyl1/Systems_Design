import math
import numpy as np
import matplotlib.pyplot as plt

#Constants
F_0 = 9.5 * 9.80665
m_tank = 73.65
f_0 = F_0/m_tank

k_a = 46646367.72 # of the propellant tank
omega_n = (k_a/m_tank)**0.5
omega_f = 100


t = np.arange(0.001, 0.3, 0.00001)

x = []

for i in t:
    x_t = (F_0/k_a)*math.cos(omega_n * i) - (f_0/(omega_n**2-omega_f**2))*(omega_n/omega_f)*math.sin(omega_n*i)+(f_0/(omega_n**2-omega_f**2))*math.sin(omega_f*i)
    x.append(x_t)

print("The F_0:", F_0)
print("The m_tank:", m_tank)
print("The f_0:", f_0)
print("The k_a:", k_a)
print("The omega_n:", omega_n)
print("The omega_f:", omega_f)

plt.plot(t, x,)
plt.title('A graph of x-t')
plt.ylabel('The displacement \'x\' [m]')
plt.xlabel('Time \'t\' [s]')
plt.grid(True)
plt.show()
