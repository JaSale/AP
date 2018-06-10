
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import stats
import pylab
Figure = pylab.figure()
Ax = Figure.gca

x, a, b = np.genfromtxt('C.txt', unpack=True)
y = a/b*2*np.pi*10**(-3)

def f(x, c):
    return np.arctan(-2*np.pi*x*c)
paramsI, covarianceI = curve_fit(f, x, y)
errorsI = np.sqrt(np.diag(covarianceI))

a = ufloat(paramsI[0], errorsI[0])
print(a)

plt.xscale("log")
L1plot = np.linspace(10, 10000, num=100000)
plt.plot(x, y,'r*', label="Messwerte")
plt.ylabel(r"$ \Delta\phi / \mathrm{rad}$" )
plt.xlabel(r"$ \nu / \mathrm{Hz}$")
plt.plot(L1plot, f(L1plot, *paramsI) , 'b-', label='Regression')
plt.tight_layout
plt.legend(loc="best")

plt.savefig('plotC.pdf')
