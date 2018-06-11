import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import stats

U, N = np.genfromtxt('3.txt' , unpack = True)
sN=(np.sqrt(N*60)/60)*10**(-1)
plt.errorbar(U, N, yerr=sN, fmt='.b', label = 'Messwerte mit Fehlerbalken')

#x, y = np.genfromtxt('2.txt' , unpack=True)
#
#def f(x, a, b):
#    return x*a + b
#paramsI, covarianceI = curve_fit(f, x, y)
#errorsI = np.sqrt(np.diag(covarianceI))
#a = ufloat(paramsI[0], errorsI[0])
#b = ufloat(paramsI[1], errorsI[1])
#print(a, b)
#
#L1plot = np.linspace(370 , 600)
plt.xlabel(r'U / V') #hier wurde Tex Code verwendet, um Brueche ordentlich darzustellen. das T_P macht, dass das P als Indesx von T erscheint. Hinter den Slash kommt die Einheit fuer die jeweilige Groesse
plt.ylabel(r"$\frac{\Delta Q}{e_0}$ ")
#plt.axvline(x=370, color='y', label='Beginn der Plateauphase')
#plt.axvline(x=610, color='g', label = 'Beginn der Entladungsphase')
#plt.plot(L1plot, f(L1plot, *paramsI) , 'r-', label='Regression') #b- macht eine blaue durchgezogene Linie
plt.tight_layout #macht irgendwas schoener. einfach dran machen...
plt.legend(loc="best")

plt.savefig('3.pdf')


#a=0.6+/-0.5, b= (1.133+/-0.025)e+04
