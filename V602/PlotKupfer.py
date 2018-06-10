import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import stats

x, y = np.genfromtxt('Messung2.txt' , unpack=True)
plt.plot(x, y, 'b-')


plt.xlabel(r"$ 2\theta / \mathrm{°}$")
plt.ylabel(r"$R / \mathrm{\frac{1}{s}} $")
plt.axvline(x=40, ymin=0, ymax = 3500, color='k', linestyle='--', label=r"$K_{\beta}$")
plt.axvline(x=44.4, ymin=0, ymax = 3500, color='g', linestyle='-.', label=r"$K_{\alpha}$")
plt.tight_layout()
plt.legend(loc="best")

plt.savefig('Kupfer.pdf')
