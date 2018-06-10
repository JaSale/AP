import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import stats

#Nullmessung1 240s N=216
N_U_Fehler = 216**(1/2)/240
N_U = 216/240

t1, N_mitU1 = np.genfromtxt('Rhodium.txt', unpack=True)
t2, N_mitU2 = np.genfromtxt('Rhodium2.txt', unpack=True)
t3, N_mitU3 = np.genfromtxt('Rhodium3.txt', unpack=True)

#Subtraktion der Untergrundstrahlung + Fehlerrechnung
N1 = N_mitU1 - N_U*20
lnN1 = np.log(N1)
N_Fehler1 = (N_mitU1 + (N_U_Fehler*20)**2)**(1/2)
lnN_Fehler1 = 1/N1*N_Fehler1
#weiterzurechen: lnN2 und lnN_Fehler2
N2 = N_mitU2 - N_U*20
N_Fehler2 = (N_mitU2 + (N_U_Fehler*20)**2)**(1/2)
lnN2 = np.log(N2)
lnN_Fehler2 = 1/N2*N_Fehler2
#weiterzurechen: lnN2 und lnN_Fehler2

L1plot = np.linspace(0, 850)
def f1(t2, l2, b2):
    return l2*t2+b2
paramsI, covarianceI = curve_fit(f1, t2, lnN2)
errorsI = np.sqrt(np.diag(covarianceI))
b2 = ufloat(paramsI[1], errorsI[1])
b2_Fehler = errorsI[1]
l2 = ufloat(paramsI[0], errorsI[0])
l2_Fehler = errorsI[0]
plt.plot(L1plot, f1(L1plot, *paramsI) , 'k-', label = "Lineare Regressionn des langsamen Zerfalls")
print('b', b2)
N_02 = unp.exp(b2)
b2 = unp.nominal_values(b2)                     #Wert N_02
b2_ohneFehler = unp.nominal_values(b2)
N_02_Fehler = np.exp(b2)*b2_Fehler      #Fehler N_02
N_U_mitFehler=ufloat(N_U, N_U_Fehler)
print('Untergundstrahlung pro Sekunde: ', N_U_mitFehler)

print('N_02: ', N_02)
print('lambda2: ', l2)
T2= np.log(0.5)/l2
print('T2= ', T2)

N3 = N_mitU3 - N_U*20
N_Fehler3 = (N_mitU3 + (N_U_Fehler*20)**2)**(1/2)
l2 = unp.nominal_values(l2)

N_02 = unp.nominal_values(N_02)
N3 = N3- N_02*np.exp(l2*t3)
a=np.exp(l2*t3)
N_Fehler3 = np.sqrt((a*N_02_Fehler)**2+(N_Fehler3)**2+(N_02*t3*l2_Fehler*a)**2)
lnN3 = np.log(N3)
lnN_Fehler3 = 1/N3*N_Fehler3

L2plot = np.linspace(0, 200)
def f2(t3, l3, b3):
    return l3*t3+b3
paramsI, covarianceI = curve_fit(f2, t3, lnN3)
errorsI = np.sqrt(np.diag(covarianceI))
b3 = ufloat(paramsI[1], errorsI[1])
l3 = ufloat(paramsI[0], errorsI[0])
print('b3', b3)
N_03 = unp.exp(b3)
print('N_03: ', N_03)
print('lambda3: ', l3)
T3= np.log(0.5)/l3
print('T3= ', T3)

l3 = unp.nominal_values(l3)
N_03 = unp.nominal_values(N_03)

x1 = np.round_(N_mitU3, decimals=3)
N_mitU3_Fehler= N_mitU3**(1/2)
x2 = np.round_(N_mitU3_Fehler, decimals=3)
y1 = np.round_(N3, decimals=3)
y2 = np.round_(N_Fehler3, decimals=3)
z1 = np.round_(lnN3, decimals=3)
z2 = np.round_(lnN_Fehler3, decimals=3)

np.savetxt('Rhodiumtabelle2.txt', np.column_stack([t3, x1, x2, y1, y2, z1, z2]),
            delimiter=' & ', newline= r' \\'+'\n', fmt='%.2f')


x = np.linspace(0, 750) # gibt 50 Zahlen in gleichmäßigem Abstand von 0–1
plt.plot(x, np.log(N_03*np.exp(l3*x)+N_02*np.exp(l2*x)), 'g--', label = "Beide Zerfälle")

plt.errorbar(t1, lnN1, yerr=lnN_Fehler1, fmt='.b', label = "Messwerte mit Fehlerbalken")
plt.errorbar(t3, lnN3, yerr=lnN_Fehler3, fmt= 'xm', label = "Schneller Zerfall" )
plt.plot(L2plot, f2(L2plot, *paramsI) , 'r-', label = "Lineare Regression des schnellen Zerfalls")
plt.xlabel(r"$ t / \mathrm{s}$")
plt.ylabel(r"$ \mathrm{ln(N_{\Delta t \, Rhodium})} $")
plt.tight_layout()
plt.legend(loc="best")
plt.savefig('Rhodium2.pdf')
