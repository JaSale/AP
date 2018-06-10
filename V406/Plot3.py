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
dDoppel, iDoppel = np.genfromtxt('Messung3.txt', unpack=True)


# Umrechnen in nA
iDoppel = (iDoppel-0.008)*10**(3) #in Ampere
dDoppel = (dDoppel - 24.79)*10**(-3)
phiDoppel = np.arctan(dDoppel/L)
# Konstanten definieren

#Fit

def g (phiDoppel, A0, s, b):
    return  (A0**2) * np.cos(np.pi*s*np.sin(phiDoppel)/wellenlaenge)**2 * (wellenlaenge/(np.pi*b*np.sin(phiDoppel)))**2 * np.sin(np.pi*b*np.sin(phiDoppel)/wellenlaenge)**2

paramsDoppel, covarianceDoppel = curve_fit(g, phiDoppel, iDoppel, p0=[80 , 0.0005, 0.000015])
errorsDoppel = np.sqrt(np.diag(covarianceDoppel))
b = ufloat(paramsDoppel[2], errorsDoppel[2])
A0 = ufloat(paramsDoppel[0], errorsDoppel[0])
s = ufloat(paramsDoppel[1], errorsDoppel[1])

print("b: ",b)
print("s: ",s)

xDoppel = np.linspace(-0.012, 0.012, 10000)
plt.figure(1)
plt.xlim(-0.012, 0.012)
plt.xlabel(r"$\varphi/\mathrm{rad}$")
plt.ylabel(r"$I/\mathrm{nA}$")
plt.plot(phiDoppel, iDoppel, 'r+', label="Messwerte")
plt.plot(xDoppel, g(xDoppel, *paramsDoppel), 'b', label="Regression Doppelspalt")
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("doppel.pdf")
