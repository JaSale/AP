import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp

f, a, b, U= np.genfromtxt('polar.txt', unpack=True)



def H(x, c):
    return -np.sin(c)/x

phi = a/b * 10 ** (-3)  * 2 *np.pi # das hier ist einfach wieder nur die Umrechnung wie vorher
A = U/980 # wieder nur geteilt durch die anfangsamplitude
plt.figure(2)
plt.polar(phi, A, 'rx', label="Messwerte")
x = np.linspace(0.00001,  2, 1000)
plt.polar(x, H(-np.tan(x), x), 'b-', label="Theoriekurve")
plt.legend(loc="lower left")
plt.tight_layout

plt.savefig('Polar2.pdf')
