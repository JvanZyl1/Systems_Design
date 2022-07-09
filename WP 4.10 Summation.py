Type = ["Heaxagonal, Nut", "Cylindrical, Nut", "Hexagonal, Thread", "Cylindrical, Thread"]
Constant = [22/3, 47/6, 49/6, 26/3]
Materials = ["Titanium", "Steel", "A286", "Monel", "Copper", "Brass", "Stainless steel", "Nickel"]
E_list = [120000000000,200000000000,201000000000,179000000000, 117000000000, 100000000000, 180000000000, 205000000000]

print("Are materials list is as following", Materials)

delta_bHN = []

for E in E_list:
    deltabHN =[]
    for numbers in range(246, 346):
        numbers = numbers/100
        deltabHN.append(Constant[0]*(1/E)*(1/numbers))
        delta_bHN.append(deltabHN)

max_bHN = max(delta_bHN)
min_bHN = min(delta_bHN)
print("For a", Type[0], "joint, the range of delta b is:", min_bHN, "-", max_bHN)

delta_bCN = []

for E in E_list:
    deltabCN =[]
    for numbers in range(246, 346):
        numbers = numbers/100
        deltabCN.append(Constant[1]*(1/E)*(1/numbers))
        delta_bCN.append(deltabCN)

max_bCN = max(delta_bCN)
min_bCN = min(delta_bCN)
print("For a", Type[1], "joint, the range of delta b is:", min_bCN, "-", max_bCN)

delta_bHT = []

for E in E_list:
    deltabHT =[]
    for numbers in range(246, 346):
        numbers = numbers/100
        deltabHT.append(Constant[2]*(1/E)*(1/numbers))
        delta_bHT.append(deltabHT)

max_bHT = max(delta_bHT)
min_bHT = min(delta_bHT)
print("For a", Type[2], "joint, the range of delta b is:", min_bHT, "-", max_bHT)

delta_bCT = []

for E in E_list:
    deltabCT =[]
    for numbers in range(246, 346):
        numbers = numbers/100
        deltabCT.append(Constant[3]*(1/E)*(1/numbers))
        delta_bCT.append(deltabCT)

max_bCT = max(delta_bCT)
min_bCT = min(delta_bCT)
print("For a", Type[3], "joint, the range of delta b is:", min_bCT, "-", max_bCT)


#print(Type[0], delta_bHN)
#print(Type[1], delta_bCN)
#print(Type[2], delta_bHT)
#print(Type[3], delta_bCT)

#Delta A

Ea = 69000000000#known
t = 0.003#known
Dfo = 0.0028#Seppe can calculate
Dfi = 0.0020#Seppe can calculate
pi = 3.14159265359
deltaa = (4*t)/(Ea*pi*(Dfo**2-Dfi**2))
print("Delta_a is", deltaa)

chi_minti = []
chi_maxti = []
chi_minst = []
chi_maxst = []
chi_minA = []
chi_maxA = []
chi_maxcu = []
chi_mincu = []
chi_minbr = []
chi_maxbr = []
chi_minss = []
chi_maxss = []
chi_minmo = []
chi_maxmo = []
chi_minni = []
chi_maxni = []

#Titanium
delta_bti = []
delta_bti.append(delta_bHN[0])
delta_bti.append(delta_bCN[0])
delta_bti.append(delta_bHT[0])
delta_bti.append(delta_bCT[0])
max_bti = max(delta_bti)
chi_timina = (deltaa)/(max_bti[0] + deltaa)
chi_timinb = (deltaa)/(max_bti[1] + deltaa)
chi_timinc = (deltaa)/(max_bti[2] + deltaa)
chi_minti.append(chi_timina)
chi_minti.append(chi_timinb)
chi_minti.append(chi_timinc)
min_bti = min(delta_bti)
chi_timaxa = (deltaa)/(max_bti[0]+ deltaa)
chi_timaxb = (deltaa)/(max_bti[1]+ deltaa)
chi_timaxc = (deltaa)/(max_bti[2]+ deltaa)
chi_maxti.append(chi_timaxa)
chi_maxti.append(chi_timaxb)
chi_maxti.append(chi_timaxc)

print("The value's for deflection deltab of", Materials[0]," in the range results from", min_bti, "-", max_bti)
print("The force ratio of", Materials[0], "in the range results from", chi_minti, "-", chi_maxti)

#Steel

delta_bst = []
delta_bst.append(delta_bHN[3])
delta_bst.append(delta_bCN[3])
delta_bst.append(delta_bHT[3])
delta_bst.append(delta_bCT[3])
max_bst = max(delta_bst)
min_bst = min(delta_bst)
chi_stmina = (deltaa)/(max_bst[0] + deltaa)
chi_stminb = (deltaa)/(max_bst[1] + deltaa)
chi_stminc = (deltaa)/(max_bst[2] + deltaa)
chi_minst.append(chi_stmina)
chi_minst.append(chi_stminb)
chi_minst.append(chi_stminc)
chi_stmaxa = (deltaa)/(max_bst[0]+ deltaa)
chi_stmaxb = (deltaa)/(max_bst[1]+ deltaa)
chi_stmaxc = (deltaa)/(max_bst[2]+ deltaa)
chi_maxst.append(chi_stmaxa)
chi_maxst.append(chi_stmaxb)
chi_maxst.append(chi_stmaxc)

print("The value's for deflection deltab of", Materials[1]," in the range results from", min_bst, "-", max_bst)
print("The force ratio of", Materials[1], "in the range results from", chi_minst, "-", chi_maxst)

#A286

delta_bA = []
delta_bA.append(delta_bHN[6])
delta_bA.append(delta_bCN[6])
delta_bA.append(delta_bHT[6])
delta_bA.append(delta_bCT[6])
max_bA = max(delta_bA)
min_bA = min(delta_bA)
chi_Amina = (deltaa)/(max_bA[0] + deltaa)
chi_Aminb = (deltaa)/(max_bA[1] + deltaa)
chi_Aminc = (deltaa)/(max_bA[2] + deltaa)
chi_minA.append(chi_Amina)
chi_minA.append(chi_Aminb)
chi_minA.append(chi_Aminc)
chi_Amaxa = (deltaa)/(max_bA[0]+ deltaa)
chi_Amaxb = (deltaa)/(max_bA[1]+ deltaa)
chi_Amaxc = (deltaa)/(max_bA[2]+ deltaa)
chi_maxA.append(chi_Amaxa)
chi_maxA.append(chi_Amaxb)
chi_maxA.append(chi_Amaxc)

print("The value's for deflection deltab of", Materials[2]," in the range results from", min_bA, "-", max_bA)
print("The force ratio of", Materials[2], "in the range results from", chi_minA, "-", chi_maxA)

#Monel

delta_bmo = []
delta_bmo.append(delta_bHN[9])
delta_bmo.append(delta_bCN[9])
delta_bmo.append(delta_bHT[9])
delta_bmo.append(delta_bCT[9])
max_bmo = max(delta_bmo)
min_bmo = min(delta_bmo)
chi_momina = (deltaa)/(max_bmo[0] + deltaa)
chi_mominb = (deltaa)/(max_bmo[1] + deltaa)
chi_mominc = (deltaa)/(max_bmo[2] + deltaa)
chi_minmo.append(chi_momina)
chi_minmo.append(chi_mominb)
chi_minmo.append(chi_mominc)
chi_momaxa = (deltaa)/(max_bmo[0]+ deltaa)
chi_momaxb = (deltaa)/(max_bmo[1]+ deltaa)
chi_momaxc = (deltaa)/(max_bmo[2]+ deltaa)
chi_maxmo.append(chi_momaxa)
chi_maxmo.append(chi_momaxb)
chi_maxmo.append(chi_momaxc)

print("The value's for deflection deltab of", Materials[3]," in the range results from", min_bmo, "-", max_bmo)
print("The force ratio of", Materials[3], "in the range results from", chi_minmo, "-", chi_maxmo)

#Copper

delta_bcu = []
delta_bcu.append(delta_bHN[12])
delta_bcu.append(delta_bCN[12])
delta_bcu.append(delta_bHT[12])
delta_bcu.append(delta_bCT[12])
max_bcu = max(delta_bcu)
min_bcu = min(delta_bcu)
chi_cumina = (deltaa)/(max_bcu[0] + deltaa)
chi_cuminb = (deltaa)/(max_bcu[1] + deltaa)
chi_cuminc = (deltaa)/(max_bcu[2] + deltaa)
chi_mincu.append(chi_cumina)
chi_mincu.append(chi_cuminb)
chi_mincu.append(chi_cuminc)
chi_cumaxa = (deltaa)/(max_bcu[0]+ deltaa)
chi_cumaxb = (deltaa)/(max_bcu[1]+ deltaa)
chi_cumaxc = (deltaa)/(max_bcu[2]+ deltaa)
chi_maxcu.append(chi_cumaxa)
chi_maxcu.append(chi_cumaxb)
chi_maxcu.append(chi_cumaxc)

print("The value's for deflection deltab of", Materials[4]," in the range results from", min_bcu, "-", max_bcu)
print("The force ratio of", Materials[4], "in the range results from", chi_mincu, "-", chi_maxcu)

#Brass

delta_bbr = []
delta_bbr.append(delta_bHN[15])
delta_bbr.append(delta_bCN[15])
delta_bbr.append(delta_bHT[15])
delta_bbr.append(delta_bCT[15])
max_bbr = max(delta_bbr)
min_bbr = min(delta_bbr)
chi_brmina = (deltaa)/(max_bbr[0] + deltaa)
chi_brminb = (deltaa)/(max_bbr[1] + deltaa)
chi_brminc = (deltaa)/(max_bbr[2] + deltaa)
chi_minbr.append(chi_brmina)
chi_minbr.append(chi_brminb)
chi_minbr.append(chi_brminc)
chi_brmaxa = (deltaa)/(max_bbr[0]+ deltaa)
chi_brmaxb = (deltaa)/(max_bbr[1]+ deltaa)
chi_brmaxc = (deltaa)/(max_bbr[2]+ deltaa)
chi_maxbr.append(chi_brmaxa)
chi_maxbr.append(chi_brmaxb)
chi_maxbr.append(chi_brmaxc)

print("The value's for deflection deltab of", Materials[5]," in the range results from", min_bbr, "-", max_bbr)
print("The force ratio of", Materials[5], "in the range results from", chi_minbr, "-", chi_maxbr)

#Stainless steel

delta_bss = []
delta_bss.append(delta_bHN[18])
delta_bss.append(delta_bCN[18])
delta_bss.append(delta_bHT[18])
delta_bss.append(delta_bCT[18])
max_bss = max(delta_bss)
min_bss = min(delta_bss)
chi_ssmina = (deltaa)/(max_bss[0] + deltaa)
chi_ssminb = (deltaa)/(max_bss[1] + deltaa)
chi_ssminc = (deltaa)/(max_bss[2] + deltaa)
chi_minss.append(chi_ssmina)
chi_minss.append(chi_ssminb)
chi_minss.append(chi_ssminc)
chi_ssmaxa = (deltaa)/(max_bss[0]+ deltaa)
chi_ssmaxb = (deltaa)/(max_bss[1]+ deltaa)
chi_ssmaxc = (deltaa)/(max_bss[2]+ deltaa)
chi_maxss.append(chi_ssmaxa)
chi_maxss.append(chi_ssmaxb)
chi_maxss.append(chi_ssmaxc)

print("The value's for deflection deltab of", Materials[6]," in the range results from", min_bss, "-", max_bss)
print("The force ratio of", Materials[6], "in the range results from", chi_minss, "-", chi_maxss)

#Nickel

delta_bni = []
delta_bni.append(delta_bHN[21])
delta_bni.append(delta_bCN[21])
delta_bni.append(delta_bHT[21])
delta_bni.append(delta_bCT[21])
max_bni = max(delta_bni)
min_bni = min(delta_bni)
chi_nimina = (deltaa)/(max_bni[0] + deltaa)
chi_niminb = (deltaa)/(max_bni[1] + deltaa)
chi_niminc = (deltaa)/(max_bni[2] + deltaa)
chi_minni.append(chi_nimina)
chi_minni.append(chi_niminb)
chi_minni.append(chi_niminc)
chi_nimaxa = (deltaa)/(max_bni[0]+ deltaa)
chi_nimaxb = (deltaa)/(max_bni[1]+ deltaa)
chi_nimaxc = (deltaa)/(max_bni[2]+ deltaa)
chi_maxni.append(chi_nimaxa)
chi_maxni.append(chi_nimaxb)
chi_maxni.append(chi_nimaxc)

print("The value's for deflection deltab of", Materials[7]," in the range results from", min_bni, "-", max_bni)
print("The force ratio of", Materials[7], "in the range results from", chi_minni, "-", chi_maxni)

chi_min = []
chi_min.append(chi_minti)
chi_min.append(chi_minst)
chi_min.append(chi_minA)
chi_min.append(chi_minmo)
chi_min.append(chi_mincu)
chi_min.append(chi_minbr)
chi_min.append(chi_minss)
chi_min.append(chi_minni)

#print("The minimum force ratios:", chi_min)

chi_max = []
chi_min.append(chi_maxti)
chi_min.append(chi_maxst)
chi_min.append(chi_maxA)
chi_min.append(chi_maxmo)
chi_min.append(chi_maxcu)
chi_min.append(chi_maxbr)
chi_min.append(chi_maxss)
chi_min.append(chi_maxni)

#print("The maximum force ratios:", chi_max)

############################Thermal ######################################

alpha_c = 0.000012 #Steel
alpha_c2 = 0.0000236 #Aluminium
deltaT_MAX = 5
deltaT_MIN = 5
A_sm = pi * (0.001)**2
alpha_b = [0.0000085, 0.000012, 0.000017, 0.000014, 0.000017, 0.000019, 0.000017, 0.000013]

#Hexagonal and Nut
constant = 22/3
delta_bh = []
delta_b = []

for E in E_list:
    deltab =[]
    for number in range(246, 346):
        number = number/100
        deltab.append(constant * (1/E) * (1/number))
        delta_bh.append(deltab)

delta_b.append(delta_bh[0])
delta_b.append(delta_bh[3])
delta_b.append(delta_bh[6])
delta_b.append(delta_bh[9])
delta_b.append(delta_bh[12])
delta_b.append(delta_bh[15])
delta_b.append(delta_bh[18])
delta_b.append(delta_bh[21])

print("Delta b for the Hexagonal bolt and Nut is: ", delta_b)

#Back to thermal

F_delta = []

#Titanium:
F_deltati = []
for i in range(0,3):
    F_ti = (alpha_c - alpha_b[0])*deltaT_MAX*E_list[0]*A_sm*(1-chi_minti[i])
    F_deltati.append(F_ti)
    
print("The following display the thermal forces due to the lug on the bolt")
print("The thermal force for", Materials[0], "is:", F_deltati)

#Steel:
F_deltast = []
for i in range(0,3):
    F_st = (alpha_c - alpha_b[1])*deltaT_MAX*E_list[1]*A_sm*(1-chi_minst[i])
    F_deltast.append(F_st)

print("The thermal force for", Materials[1], "is:", F_deltast)

#A286
F_deltaA = []
for i in range(0,3):
    F_A = (alpha_c - alpha_b[2])*deltaT_MAX*E_list[2]*A_sm*(1-chi_minA[i])
    F_deltaA.append(F_A)

print("The thermal force for", Materials[2], "is:", F_deltaA)

#Monel
F_deltamo = []
for i in range(0,3):
    F_mo = (alpha_c - alpha_b[3])*deltaT_MAX*E_list[3]*A_sm*(1-chi_minmo[i])
    F_deltamo.append(F_mo)

print("The thermal force for", Materials[3], "is:", F_deltamo)

#Copper
F_deltacu = []
for i in range(0,3):
    F_cu = (alpha_c - alpha_b[4])*deltaT_MAX*E_list[4]*A_sm*(1-chi_mincu[i])
    F_deltacu.append(F_cu)

print("The thermal force for", Materials[4], "is:", F_deltacu)

#Brass
F_deltabr = []
for i in range(0,3):
    F_br = (alpha_c - alpha_b[5])*deltaT_MAX*E_list[5]*A_sm*(1-chi_minbr[i])
    F_deltabr.append(F_br)

print("The thermal force for", Materials[5], "is:", F_deltabr)

#Stainless Steel
F_deltass = []
for i in range(0,3):
    F_ss = (alpha_c - alpha_b[6])*deltaT_MAX*E_list[6]*A_sm*(1-chi_minss[i])
    F_deltass.append(F_ss)

print("The thermal force for", Materials[6], "is:", F_deltass)

#Nickel
F_deltani = []
for i in range(0,3):
    F_ni = (alpha_c - alpha_b[7])*deltaT_MAX*E_list[7]*A_sm*(1-chi_minst[i])
    F_deltani.append(F_ni)

print("The thermal force for", Materials[7], "is:", F_deltani)

F_delta.append(F_deltati)
F_delta.append(F_deltast)
F_delta.append(F_deltaA)
F_delta.append(F_deltamo)
F_delta.append(F_deltacu)
F_delta.append(F_deltabr)
F_delta.append(F_deltass)
F_delta.append(F_deltani)
#F_deltamin = min(F_delta)
#F_deltamax = max(F_delta)

#print("The F_delta,t,max is equal to F_delta,t,min and:", F_delta)
#print("The minimum F_delta,t,max", F_deltamin, "and the maximum", F_deltamax)

alpha_c2 = 0.0000236 #Aluminium

#Titanium:
F_deltati2 = []
for i in range(0,3):
    F_ti = (alpha_c2 - alpha_b[0])*deltaT_MAX*E_list[0]*A_sm*(1-chi_minti[i])
    F_deltati2.append(F_ti)
    
print("The following display the thermal forces due to the wall on the bolt")
print("The thermal force for", Materials[0], "is:", F_deltati2)

#Steel:
F_deltast2 = []
for i in range(0,3):
    F_st = (alpha_c2 - alpha_b[1])*deltaT_MAX*E_list[1]*A_sm*(1-chi_minst[i])
    F_deltast2.append(F_st)

print("The thermal force for", Materials[1], "is:", F_deltast2)

#A286
F_deltaA2 = []
for i in range(0,3):
    F_A = (alpha_c2 - alpha_b[2])*deltaT_MAX*E_list[2]*A_sm*(1-chi_minA[i])
    F_deltaA2.append(F_A)

print("The thermal force for", Materials[2], "is:", F_deltaA2)

#Monel
F_deltamo2 = []
for i in range(0,3):
    F_mo = (alpha_c2 - alpha_b[3])*deltaT_MAX*E_list[3]*A_sm*(1-chi_minmo[i])
    F_deltamo2.append(F_mo)

print("The thermal force for", Materials[3], "is:", F_deltamo2)

#Copper
F_deltacu2 = []
for i in range(0,3):
    F_cu = (alpha_c2 - alpha_b[4])*deltaT_MAX*E_list[4]*A_sm*(1-chi_mincu[i])
    F_deltacu2.append(F_cu)

print("The thermal force for", Materials[4], "is:", F_deltacu2)

#Brass
F_deltabr2 = []
for i in range(0,3):
    F_br = (alpha_c2 - alpha_b[5])*deltaT_MAX*E_list[5]*A_sm*(1-chi_minbr[i])
    F_deltabr2.append(F_br)

print("The thermal force for", Materials[5], "is:", F_deltabr2)

#Stainless Steel
F_deltass2 = []
for i in range(0,3):
    F_ss = (alpha_c2 - alpha_b[6])*deltaT_MAX*E_list[6]*A_sm*(1-chi_minss[i])
    F_deltass2.append(F_ss)

print("The thermal force for", Materials[6], "is:", F_deltass2)

#Nickel
F_deltani2 = []
for i in range(0,3):
    F_ni = (alpha_c2 - alpha_b[7])*deltaT_MAX*E_list[7]*A_sm*(1-chi_minst[i])
    F_deltani2.append(F_ni)

print("The thermal force for", Materials[7], "is:", F_deltani2)

def sum_lists(*args):
    return list(map(sum, zip(*args)))

F_ti = sum_lists(F_deltati, F_deltati2)
print("The summation of Titanium's thermal forces gives:", F_ti)
F_st = sum_lists(F_deltast, F_deltast2)
print("The summation of Steel's thermal forces gives:", F_st)
F_A = sum_lists(F_deltaA, F_deltaA2)
print("The summation of A286's thermal forces gives:", F_A)
F_mo = sum_lists(F_deltamo, F_deltamo2)
print("The summation of Monel's thermal forces gives:", F_mo)
F_cu = sum_lists(F_deltacu, F_deltacu2)
print("The summation of Copper's thermal forces gives:", F_cu)
F_br = sum_lists(F_deltabr, F_deltabr2)
print("The summation of Brass's thermal forces gives:", F_br)
F_ss = sum_lists(F_deltass, F_deltass2)
print("The summation of Stainless Steel's thermal forces gives:", F_ss)
F_ni = sum_lists(F_deltani, F_deltani2)
print("The summation of Nickel's thermal forces gives:", F_ni)

#------------------------------------------------------------------Variables names from Chen--------------------------------------------------------------#

#def out_of_plane_forces_onfasteners(Fx: float, Fy: float, Fz: float, l: float, coord: tuple):
   
        #Fy = force in y direction, Fx = force in x direction, Fz = force in z direction, l = distance between the center of the backplate and the center of lug hole,
        #and coord is a tuple containing the x- and z-coordinates of the fasteners on one side of the lug.
        #Returns a tuple containing the in-plane x force, the in-plane z force and the in-plane force, created by My, for each fastener.
   
 #   Fopy = Fy / (2len(coord))

  #  Mx, Mz = Fxl, Fzl

   # denom = 2sum([z**2 for , z in coord])
    #FopMx = [-Mxz/(denom) for _, z in coord]

    #FopMz = Mzcoord[0][0] / 2len(coord)coord[0][0]

    #ForceR = [Fopy - FopMz + F for F in FopMx]
    #ForceL = [Fopy + FopMz + F for F in FopMx]

    #return max(max(ForceL), max(ForceR))

#----------------------------------------------------------------------------------------------------------------------------------------------------------#








