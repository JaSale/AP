import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import stats

Ud1 , D1_in_Zoll = np.genfromtxt('Messung1.1.txt' , unpack=True)
Ud2 , D2_in_Zoll = np.genfromtxt('Messung1.2.txt' , unpack=True)
Ud3 , D3_in_Zoll = np.genfromtxt('Messung1.3.txt' , unpack=True)
Ud4 , D4_in_Zoll = np.genfromtxt('Messung1.4.txt' , unpack=True)
Ud5 , D5_in_Zoll = np.genfromtxt('Messung1.5.txt' , unpack=True)

#umrechnen in meter
D1 = D1_in_Zoll * 0.0254 *2/8
D2 = D2_in_Zoll * 0.0254 *2/8
D3 = D3_in_Zoll * 0.0254 *2/8
D4 = D4_in_Zoll * 0.0254 *2/8
D5 = D5_in_Zoll * 0.0254 *2/8

#Beschleunigungsspannungen einlesen


plt.plot(Ud1, D1,'bo', label="Messung 1, $U_b$ = 200V")
plt.plot(Ud2, D2,'go', label="Messung 2, $U_b$ = 300V")
plt.plot(Ud3, D3,'ro', label="Messung 3, $U_b$ = 350V")
plt.plot(Ud4, D4,'co', label="Messung 4, $U_b$ = 400V")
plt.plot(Ud5, D5,'mo', label="Messung 5, $U_b$ = 450V")
plt.xlabel(r"$U_d / \mathrm{V}$")
plt.ylabel(r"$D / \mathrm{m}$")

def f1(Ud1, m1 , n1):
    return m1 * Ud1 +n1
paramsI, covarianceI = curve_fit(f1, Ud1, D1)
errorsI = np.sqrt(np.diag(covarianceI))
n1 = ufloat(paramsI[1], errorsI[1])
m1 = ufloat(paramsI[0], errorsI[0])
print("m1 = " , m1)

def f2(Ud2, m2 , n2):
    return m2 * Ud2 +n2
paramsI, covarianceI = curve_fit(f2, Ud2, D2)
errorsI = np.sqrt(np.diag(covarianceI))
m2 = ufloat(paramsI[0], errorsI[0])
n2 = ufloat(paramsI[1], errorsI[1])
print("m2 = " , m2)

def f3(Ud3, m3 , n3):
    return m3 * Ud3 +n3
paramsI, covarianceI = curve_fit(f3, Ud3, D3)
errorsI = np.sqrt(np.diag(covarianceI))
m3 = ufloat(paramsI[0], errorsI[0])
n3 = ufloat(paramsI[1], errorsI[1])
print("m3 = " , m3)

def f4(Ud4, m4 , n4):
    return m4 * Ud4 +n4
paramsI, covarianceI = curve_fit(f4, Ud4, D4)
errorsI = np.sqrt(np.diag(covarianceI))
m4 = ufloat(paramsI[0], errorsI[0])
n4 = ufloat(paramsI[1], errorsI[1])
print("m4 = " , m4)

def f5(Ud5, m5 , n5):
    return m5 * Ud5 +n5
paramsI, covarianceI = curve_fit(f5, Ud5, D5)
errorsI = np.sqrt(np.diag(covarianceI))
m5 = ufloat(paramsI[0], errorsI[0])
n5 = ufloat(paramsI[1], errorsI[1])
print("m5 = " , m5)


plt.figure(2)
#m_alle = np.uarray([m1, m2, m3, m4, m5])
m_alle , Ub = np.genfromtxt('Steigungen.txt', unpack = True)
m_alle = m_alle *10**3
Ub_Kehrwert = 1/Ub *10**3
def f6(Ub, m, n):
    return Ub*m + n
paramsI, covarianceI = curve_fit(f6, Ub_Kehrwert, m_alle)
errorsI = np.sqrt(np.diag(covarianceI))
n = ufloat(paramsI[1], errorsI[1])
m = ufloat(paramsI[0], errorsI[0])
print("m, n = ", m, n)

L1plot = np.linspace(2.1, 5.2)
plt.plot(Ub_Kehrwert, m_alle,'ro', label="Messwerte")
plt.xlabel(r"$\frac{1}{U_b} / \mathrm{\frac{1}{mV}}$")
plt.ylabel(r"$\frac{D}{U_d} / \mathrm{\frac{m}{mV}}$")
#linreg
plt.plot(L1plot, f6(L1plot, *paramsI) , 'b-', label='Lineare Regression')
plt.tight_layout()
plt.legend(loc="best")

plt.savefig('PlotSteigung1.pdf')

L = (14.3+1.03)*10**(-2)
d = (0.38+0.95)/2*10**(-2)
p = 1.9 * 10**(-2)
d = ufloat(d, 0.00403)
a_Literatur = L*p/(2*d)
m=-m
print("Literaturwert: " ,a_Literatur)
print("Berechneter Wert: ", m)

#Frequenz
v1 = 79.92
v2 = 159.77
v3 = 39.90
v4 = 26.66

t1 = 1
t2 = 0.5
t3 =  2
t4 =  3

vs1 = v1 * t1
vs2 = v2 * t2
vs3 = v3 * t3
vs4 = v4 * t4

print("vs1= ", vs1)
print("vs2= ", vs2)
print("vs3= ", vs3)
print("vs3= ", vs4)

v = (vs1+vs2+vs3+vs4)/4
deltav = (((vs1-v)**2+(vs2-v)**2+(vs3-v)**2+(vs4-v)**2)/4/3)**(1/2)

print("v =", v, deltav)

c = ufloat(-0.3176, 0.0029)
U = 350
A = ufloat(0.0109, 0.0007)
Ud = A *U /c
print('Ud = ', Ud)
