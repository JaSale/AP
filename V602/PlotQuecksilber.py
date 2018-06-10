import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import stats

x, y = np.genfromtxt('Quecksilber.txt' , unpack=True)
plt.plot(x, y, 'b-')


plt.xlabel(r"$ 2\theta / \mathrm{°}$")
plt.ylabel(r"$R / \mathrm{\frac{1}{s}} $")
plt.axvline(x=25, ymin=0, ymax = 25, color='k', linestyle='--', label='$K_{L2}$')
plt.axvline(x=29, ymin=0, ymax = 25, color='g', linestyle='-.', label='$K_{L3}$')
plt.tight_layout()
plt.legend(loc="best")

plt.savefig('Quecksilber.pdf')
