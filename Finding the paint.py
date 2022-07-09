import math
import numpy as np
import matplotlib.pyplot as plt

Js = 1356 #W/m^2
As = 6.75 #m^2
Ja = 734.45 #W/m^2
Aa = 6.75 #m^2
Jp = 229.73 #W/m^2
Ap = 6.75 #W/m^2
Qmin = 121.529#W
Qmax = 218 #W
sigma = 5.67*(10**(-8)) #cba
Ae = 26 #m^2

alpha = 0.08 #constant
epsilon = 0.04

T = ((Js*As*alpha + Ja*Aa*alpha + Jp*epsilon*Ap + Qmin)/(sigma*epsilon*Ae))**0.25
T2 = ((Js*As*alpha + Ja*Aa*alpha + Jp*epsilon*Ap + Qmax)/(sigma*epsilon*Ae))**0.25

print("The temperature at minimum internal heat is", T)
print("The temperature at maximum internal heat is", T2)
