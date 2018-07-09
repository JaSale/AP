import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat
from uncertainties.umath import sqrt

x, y = np.genfromtxt('a.txt', unpack=True)

def f(x, a, b):
    return a*x**2+b
def g(x, e, d):
    return e+d/x**2


paramsI, covarianceI = curve_fit(f, x, y)
paramsII, covarianceII = curve_fit(g, x, y)
errorsI = np.sqrt(np.diag(covarianceI))
errorsII = np.sqrt(np.diag(covarianceII))
a = ufloat(paramsI[0], errorsI[0])
b = ufloat(paramsI[1], errorsI[1])
d = ufloat(paramsII[0], errorsII[0])
e = ufloat(paramsII[1], errorsII[1])
L1plot = np.linspace(350, 700)
print("a =", a)
print("b =", b)
print("d =", d)
print("e =", e)

plt.plot(x, y, 'rx', label='Messwerte')
plt.plot(L1plot, g(L1plot, *paramsII), 'b-', label='$\mathrm{\lambda} \gg \mathrm{\lambda_1}$')
plt.plot(L1plot, f(L1plot, *paramsI), 'c-', label='$\mathrm{\lambda} \ll \mathrm{\lambda_1}$')

plt.xlabel(r'$\mathrm{\lambda}\,/\,\mathrm{nm}$')
plt.ylabel(r'$\mathrm{n^2(\lambda)}\,/\,^\circ$')
plt.xlim(350, 700)
#plt.ylim(3, 3.5)

#print('Parameter: ', params, '\nFehler: ', np.sqrt(np.diag(cov)))
plt.legend(loc='best')
#plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('dispersion.pdf')
