import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import stats

x, y = np.genfromtxt('Strontium.txt' , unpack=True)
plt.plot(x, y, 'b-')


plt.xlabel(r"$ 2\theta / \mathrm{°}$")
plt.ylabel(r"$R / \mathrm{\frac{1}{s}} $")
plt.axvline(x=21.7, color='k', linestyle='--', label='$K-Kante$')
plt.tight_layout()
plt.legend(loc="best")

plt.savefig('Strontium.pdf')
