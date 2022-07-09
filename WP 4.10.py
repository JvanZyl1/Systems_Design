Materials = ["Titanium", "Steel", "A286", "Monel", "Copper", "Brass", "Stainless steel", "Nickel"]
E_list = [120000000000,200000000000,201000000000,179000000000, 117000000000, 100000000000, 180000000000, 205000000000]
results = []
chi =[]

Ea = 2#known
t = 2#known
Dfo = 3#Seppe can calculate
Dfi = 2#Seppe can calculate
pi = 3.14159265359
deltaa = (4*t)/(Ea*pi*(Dfo**2-Dfi**2))
summin = 0#known
summax = 4#known

for E in E_list:
    interim_resutls = []
    interim_chi = []
    for number in range(summin, summax): #change the range number, remember is divided by 1000)
        number = number/1000
        interim_resutls.append((1/E)*number)
        interim_chi.append(deltaa/(deltaa+((1/E)*number)))
    results.append(interim_resutls)
    chi.append(interim_chi)

print("The materials are displayed as followed", Materials)
print("The deflection delta_a is a constant", deltaa)
print("The value's for deflection deltab in the range results from", results)
print("The value of the force ratio chi is", chi)
