E_list = [120000000000,200000000000,201000000000]
Materials = ["Titanium", "Steel", "A286"]
constant = 22/3

delta_b = []

for E in E_list:
    deltab =[]
    for number in range(19,22):
        number = number/10
        deltab.append(constant * (1/E) * (1/number))
        delta_b.append(deltab)

print(delta_b)
