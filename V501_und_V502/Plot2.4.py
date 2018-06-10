import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import stats

R = 0.282
N = 20
L = 17.5 *10**(-2)

I1 , I2, I3, I5, D1 = np.genfromtxt('Messung2.1.txt', unpack = True)
I4, D2 = np.genfromtxt('Messung2.2.txt', unpack = True)

D1 = D1 * 0.0254 *2/8
D2 = D2 * 0.0254 *2/8
mu = 4 * np.pi *10**(-7)

B1 = mu * 8/(125**(1/2)) * N * I1 /R *10**(3)
B2 = mu * 8/(125**(1/2)) * N * I2 /R *10**3
B3 = mu * 8/(125**(1/2)) * N * I3 /R *10**3
B4 = mu * 8/(125**(1/2)) * N * I4 /R *10**3
B5 = mu * 8/(125**(1/2)) * N * I5 /R *10**3

A1 = D1 /(L**2 + D1**2)
A2 = D2 /(L**2 + D2**2)

plt.figure(1)
L1plot = np.linspace(0,0.21)

#plt.plot(B1, A1,'bo', label="Messwerte")
#plt.plot(B2, A1,'bo', label="Messwerte")
#plt.plot(B3, A1,'bo', label="Messwerte")
plt.plot(B4, A2,'bo', label="Messwerte")
#plt.plot(B5, A1,'bo', label="Messwerte")

plt.xlabel(r"$B / \mathrm{mT}$")
plt.ylabel(r"$\frac{D}{D^2+L^2} / \mathrm{\frac{1}{m}}$")

def f4(B4, m4 , n4):
    return m4 * B4 +n4
paramsI, covarianceI = curve_fit(f4, B4, A2)
errorsI = np.sqrt(np.diag(covarianceI))
n4 = ufloat(paramsI[1], errorsI[1])
m4 = ufloat(paramsI[0], errorsI[0])

plt.plot(L1plot, f4(L1plot, *paramsI) , 'g-', label = "Lineare Regression")

plt.tight_layout()
plt.legend(loc="best")

plt.savefig('Plot2.4.pdf')
