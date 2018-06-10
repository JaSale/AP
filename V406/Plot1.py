import numpy as np
import matplotlib.pyplot as plt
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import stats
import scipy.constants as const
plt.rcParams['figure.figsize'] = (10, 8)
plt.rcParams['font.size'] = 18

L = 1.12 #in m
wellenlaenge = 633*10**(-9)

#Einlesen der Daten
#Einfach Spalt
dEinzel, iEinzel = np.genfromtxt('Messung1.txt', unpack=True)
# Umrechnen in nA
iEinzel = (iEinzel-0.008)*10**(3) #in Ampere
dEinzel = (dEinzel - 24.74)*10**(-3)
phiEinzel = np.arctan(dEinzel/L)
# Konstanten definieren

#Fit

def g (phiEinzel, A0, b):
    return  (A0**2) * (b**2) * (wellenlaenge/(np.pi*b*np.sin(phiEinzel)))**2 * (np.sin((np.pi*b*np.sin(phiEinzel)/wellenlaenge))**2)

paramsEinzel, covarianceEinzel = curve_fit(g, phiEinzel, iEinzel, p0=[30000 , 0.00015])
errorsEinzel = np.sqrt(np.diag(covarianceEinzel))
b = ufloat(paramsEinzel[1], errorsEinzel[1])
A0 = ufloat(paramsEinzel[0], errorsEinzel[0])
#c = ufloat(paramsEinzel[2], errorsEinzel[2])
print("")
print("Einzelspalt")
print("")
print("Spaltbreite: ",b)
print("A0: ",A0)

xEinzel = np.linspace(-0.012, 0.012, 10000)
plt.figure(1)
plt.xlim(-0.012, 0.012)
plt.xlabel(r"$\varphi/\mathrm{rad}$")
plt.ylabel(r"$I/\mathrm{nA}$")
plt.plot(phiEinzel, iEinzel, 'r+', label="Messwerte")
plt.plot(xEinzel, g(xEinzel, *paramsEinzel), 'b', label="Regression")
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("einzel.pdf")
