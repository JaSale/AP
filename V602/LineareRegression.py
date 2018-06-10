import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import stats
from scipy.constants import constants

y, x = np.genfromtxt('lineareRegression.txt', unpack=True)
y = (y)**(1/2)
L1plot = np.linspace(34,41)
def f1(x, m , b):
    return x*m+b
paramsI, covarianceI = curve_fit(f1, x, y)
errorsI = np.sqrt(np.diag(covarianceI))
b = ufloat(paramsI[1], errorsI[1])
m = ufloat(paramsI[0], errorsI[0])

plt.xlabel(r"$z$")
plt.ylabel(r"$\sqrt{E_K} / \sqrt{eV}$")
plt.plot(x, y,'bo', label="Messwerte")
plt.plot(L1plot, f1(L1plot, *paramsI) , 'g-', label="Lineare Regression")
plt.tight_layout()
plt.legend(loc="best")
plt.savefig('Lineare Regression.pdf')
