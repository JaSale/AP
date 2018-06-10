import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import stats

x, y = np.genfromtxt('Halbwärtsbreite.txt' , unpack=True)
plt.plot(x, y, 'b-')


plt.xlabel(r"$ 2\theta / \mathrm{°}$")
plt.ylabel(r"$R / \mathrm{\frac{1}{s}} $")
plt.axhline(y=1695, xmin=0.23, xmax=0.80, linestyle='-.', color = 'k', label='$y=1695$')
plt.axvline(x=44.18, color='k', linestyle='--', label='$linke Seite: x=44,18$')
plt.axvline(x=44.96, color='k', linestyle='--', label='$rechte Seite: x=44,96$')
plt.tight_layout()
plt.legend(loc="best")

plt.savefig('Halbwärtsbreite2.pdf')
