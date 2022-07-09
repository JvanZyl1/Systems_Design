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

t = np.arange(0, 0.2, 0.0000001)

xh = []
xp=[]
x = []
omega_f = 100
f = 100*2*3.14159

for i in t:
    xh_0 = f_0/(omega_n**2-f**2)
    x_h = (F_0/k_a)*math.cos(omega_n*i)-xh_0*(f/omega_n)*math.sin(f*i)
    xh.append(x_h)

for i in t:
    x_p = (f_0/(omega_n**2-f**2))*math.sin(f*i)
    xp.append(x_p)

for i in t:
    xha0 = f_0/(omega_n**2-f**2)
    xah = (F_0/k_a)*math.cos(omega_n*i)-xh_0*(f/omega_n)*math.sin(f*i)
    xap = (f_0/(omega_n**2-f**2))*math.sin(f*i)
    xa = xah + xap
    x.append(xa)

#for i in t:
 #   xh_0a = f_0/(omega_n**2-f**2)
  #  x_ha = (F_0/k_a)*math.cos(omega_n*i)-xh_0a*(f/omega_n)*math.sin(f*i)
   # x_pa = (f_0/(omega_n**2-f**2))*math.sin(f*i)
    #x = x_ha + x_pa
    #xt.append(x)


plt.plot(t, xp, label="x_p")
plt.plot(t, xh, label="x_h")
plt.plot(t, x, label="x")
plt.title('t [s] vs x [m]')
plt.ylabel('x [m]]')
plt.xlabel('t [s]')
plt.legend()
plt.grid(True)
plt.show()
