import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import stats

#Nullmessung 240s N=216
N_U_Fehler = 216**(1/2)/240*20
N_U = 216/240*20

t, N_mitU = np.genfromtxt('Vanadium.txt', unpack=True)

#Subtraktion der Untergrundstrahlung + Fehlerrechnung
N = N_mitU - N_U
N_mitU_Fehler = N_mitU**(1/2)
N_Fehler = (N_mitU_Fehler**2 + N_U_Fehler**2)**(1/2)
lnN = np.log(N)
lnN_Fehler = N_Fehler/N

#linearer Fit

#plt.yscale('log')
L1plot = np.linspace(0, 1050)
def f1(t, l, b):
    return l*t+b
paramsI, covarianceI = curve_fit(f1, t, lnN)
errorsI = np.sqrt(np.diag(covarianceI))
b = ufloat(paramsI[1], errorsI[1])
l = ufloat(paramsI[0], errorsI[0])
print('l= ', l)
print('b= ', b)
#Umrechnungen und prints
N_0 = unp.exp(b)
N_U_mitFehler=ufloat(N_U, N_U_Fehler)
print('Untergundstrahlung: ', N_U_mitFehler)
print('N_0: ', N_0)
print('lambda: ', l)
T = np.log(0.5)/l
print('T1/2=', T)
#tabelle

x1 = np.round_(N_mitU, decimals=3)
x2 = np.round_(N_mitU_Fehler, decimals=3)
y1 = np.round_(N, decimals=3)
y2 = np.round_(N_Fehler, decimals=3)
z1 = np.round_(lnN, decimals=3)
z2 = np.round_(lnN_Fehler, decimals=3)

np.savetxt('Vanadiumtabelle.txt', np.column_stack([t, x1, x2, y1, y2, z1, z2]),
            delimiter=' & ', newline= r' \\'+'\n', fmt='%.2f')

#plot

plt.errorbar(t, lnN, yerr=lnN_Fehler, fmt='.b', label = "Messwerte mit Fehlerbalken")
plt.plot(L1plot, f1(L1plot, *paramsI) , 'g-', label = "Lineare Regression")
plt.xlabel(r"$ t / \mathrm{s}$")
plt.ylabel(r"$ \mathrm{ln}(N_{\mathrm{\Delta t \, Vanadium}}) $")
plt.tight_layout()
plt.legend(loc="best")
plt.savefig('Vanadium.pdf')
