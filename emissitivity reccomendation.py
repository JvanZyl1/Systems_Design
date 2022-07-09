import math
import numpy as np
import matplotlib.pyplot as plt

Js = 1356 #W/m^2
As = 6.75 #m^2
Ja = 734.45 #W/m^2
Aa = 6.75 #m^2
Jp = 229.73 #W/m^2
Ap = 6.75 #W/m^2
Q = 121.529#W
sigma = 5.67*(10**(-8)) #cba
Ae = 26 #m^2

alpha = 0.17 #constant
alpinv = 1/alpha
epsilon = np.arange(0.001, 1, 0.001)
ae = [x / alpinv for x in epsilon]
T=[]
for x in epsilon:
    T.append(((((Js*As + Ja*Aa)*alpha + Jp*x*Ap + Q)/(sigma*x*Ae))**0.25)-273.15)
    

plt.plot(epsilon, T, 'o', color = 'black')
plt.title('Choosing the correct amount of insulation layers for the paint')
plt.ylabel('Equilibirum temperature [degrees Celsius]')
plt.xlabel('Emisstivity')
plt.show()

T = 288.15 #K

e = (Js*As*alpha+Ja*Aa*alpha+Q)/((T**4)*sigma*Ae+Jp*Ap)

print(e)



