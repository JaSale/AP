import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import stats

A2_1, t2_1, A2_2, t2_2, l = np.genfromtxt('Dämpfung.txt', unpack = True)
s = 2*l*10**(-2)

L1plot = np.linspace(0, 0.25)
def f1(s, a, U_0):
    return U_0*np.exp(-a*s)
paramsI, covarianceI = curve_fit(f1, s, A2_2)
errorsI = np.sqrt(np.diag(covarianceI))
U_0 = ufloat(paramsI[1], errorsI[1])
a = ufloat(paramsI[0], errorsI[0])

plt.xlabel(r"$l/ \mathrm{m}$")
plt.ylabel(r"$U / \mathrm{V}$")
plt.plot(s, A2_2,'bo', label="Messwerte")
plt.plot(L1plot, f1(L1plot, *paramsI) , 'g-', label="Exponentielle Regression")
plt.tight_layout()
plt.legend(loc="best")

print('U_0: ', U_0)
print('a: ', a)
plt.savefig('PlotDämpfung.pdf')
