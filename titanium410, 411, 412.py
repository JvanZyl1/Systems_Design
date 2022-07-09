Type = "Heaxagonal, Nut"
Constant = 22/3
Materials = "Titanium"
E = 120000000000
alpha_b = 0.0000085
d_fo = 0.002
d_f = 0.00296
t = 0.00146*2
Ea = 69000000000
pi = 3.14159265359
deltaT = 5
alpha_c = 0.0000236


A_sm = pi * (0.001)**2

delta_a = (4*t)/(Ea*pi*(d_f**2-d_fo**2))

Delta_b = Constant*(1/E)*(1/d_fo)

phi = (delta_a)/(delta_a + Delta_b)

sigma_deltaT = (alpha_c - alpha_b)*deltaT*E*(1-phi)

F_deltaT = sigma_deltaT*A_sm

print("For", Materials, "with a", Type, "fastener:")
print("Delta_a:", delta_a)
print("Delta_b:", Delta_b)
print("Phi:", phi)
print("sigma_deltaT", sigma_deltaT)
print("Area_SM", A_sm)
print("F_deltaT", F_deltaT)
                 


