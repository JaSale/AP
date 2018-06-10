
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import stats
import pylab
Figure = pylab.figure()
Ax = Figure.gca

U = 960
x, y = np.genfromtxt('B.txt', unpack=True)
y = y/U

def f(x, a):
    return 1/np.sqrt(1+(2*np.pi*x*a)**2)
paramsI, covarianceI = curve_fit(f, x, y)
errorsI = np.sqrt(np.diag(covarianceI))

a = ufloat(paramsI[0], errorsI[0])
print(a)

plt.xscale("log")
L1plot = np.linspace(10, 10000, num=100000)
plt.plot(x, y,'r*', label="Messwerte")
plt.ylabel(r"$\frac{A(\nu)}{U_0}$" )
plt.xlabel(r"$ \nu / \mathrm{Hz}$")
plt.plot(L1plot, f(L1plot, *paramsI) , 'b-', label='Regression')
plt.tight_layout
plt.legend(loc="best")

plt.savefig('plotB.pdf')
