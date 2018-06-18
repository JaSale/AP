import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import stats

#Schall-Echo-Verfahren
A2_1, t2_1, A2_2, t2_2, l = np.genfromtxt('Dämpfung.txt', unpack = True)
s = 2*l*10**(-2)

t= (t2_2 - t2_1)/2
l=l
x1=-(0.4-30.1)/2
x2=7.08

#Durchschall-Verfahren
#t, l = np.genfromtxt('Durchschall-Verfahren.txt', unpack=True)

L1plot = np.linspace(0, 50)
def f1(t, c, b):
    return t * c +b
paramsI, covarianceI = curve_fit(f1, t, l)
errorsI = np.sqrt(np.diag(covarianceI))
b = ufloat(paramsI[1], errorsI[1])
c = ufloat(paramsI[0], errorsI[0])

plt.ylabel(r"$l/ \mathrm{cm}$")
plt.xlabel(r"$\mathrm{\Delta}t/2 \ / \mathrm{\mu s}$")
plt.plot(t, l,'bo', label="Messwerte")
plt.plot(x1, x2,'bo')
plt.plot(L1plot, f1(L1plot, *paramsI) , 'g-', label="Lineare Regression")
plt.tight_layout()
plt.legend(loc="best")

print('b: ', b)
print('c-Acryl: ', c)
plt.savefig('Schallgeschwindigkeit1.pdf')
