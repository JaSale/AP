import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import stats

U, N = np.genfromtxt('Messung1.txt', unpack=True)
N_Fehler = np.sqrt(N)
plt.errorbar(U, N, yerr=N_Fehler, fmt='.b', label = "Messwerte mit Fehlerbalken")
plt.savefig('Messung1.pdf')
