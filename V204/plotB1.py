import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import stats


Z, T_1, T_2, T_3, T_4, T_5, T_6, T_7, T_8 = np.genfromtxt('Messung1.txt' , unpack=True)
t = Z
A_1 = T_7 - T_8
A_2 = T_2 - T_1

#with plt.xkcd(): (macht, dass die ganze Sache in comic sans ms optik ausgegeben wird)
#Plot der Messwerte
#L1plot = np.linspace(0.02, 0.1) #Grenzen fuer linregr.
#plt.title('Plot Gravitationsmethode')
plt.plot(t, A_1,'r-', label="Edelstahl:T7-T8")
plt.plot(t, A_2,'b-', label="Messing:T2-T1")
plt.xlabel(r"$t / \mathrm{s}$")
plt.ylabel(r"$T / \mathrm{°C}$")

#linreg
#plt.plot(L1plot, f(L1plot, *paramsI) , 'b-', label='Lineare Regression')
plt.tight_layout
plt.legend(loc="best")

plt.savefig('plotB.pdf')
