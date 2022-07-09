import math
import numpy as np
import matplotlib.pyplot as plt

u11 = -0.4427758
u21 = -2.25845
omega1 = 955.92
omega2 = 694.82
chi1 = 1.57079632679
chi2 = 1.57079632679
A1 = 1
A2 = 1
t = np.arange(0,0.1,0.00001)
xt=[]
xtb=[]
xtc=[]

for i in t:
    x = u11*A1*math.sin(omega1*i+chi1)+u21*A2*math.sin(omega2*i+chi2)
    xt.append(x)

for i in t:
    xb = A1*math.sin(omega1*i+chi1)+A2*math.sin(omega2*i+chi2)
    xtb.append(xb)

for i in t:
    x1 = u11*A1*math.sin(omega1*i+chi1)+u21*A2*math.sin(omega2*i+chi2)
    x2 = A1*math.sin(omega1*i+chi1)+A2*math.sin(omega2*i+chi2)
    xc = x1 + x2
    xtc.append(xc)


plt.plot(t, xt, label = "x_1(t)")
plt.plot(t, xtb, label = "x_2(t)")
plt.plot(t, xtc, label = "x(t)")
plt.title('x(t) [m] vs t [s]')
plt.ylabel('x(t) [m]')
plt.xlabel('t [s]')
plt.legend()
plt.grid(True)
plt.show()
