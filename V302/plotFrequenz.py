import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import stats

x, y = np.genfromtxt('Frequenz.txt' , unpack=True)

U = 2120
y=y/U

f_0 = 240.08
x = x/f_0
def f(x, y):

    return np.sqrt(1/9* ((x)**2 - 1)**2/((1-(x)**2)**2 + 9 *(x)**2))
paramsI, covarianceI = curve_fit(f, x, y)
errorsI = np.sqrt(np.diag(covarianceI))


L1plot = np.linspace(0.08, 125, num=10000)
plt.plot(x, y,'r*', label="Messwerte") #r+, macht, dass eure Werte als rote Plusse erscheinen. mit b* kommen blaue sterne...mehr Farben kann man online finden;)
#Achsen beschriften!!!!!!

plt.plot(L1plot, f(L1plot, *paramsI) , 'b-', label='Theoriekurve') #b- macht eine blaue durchgezogene Linie
plt.tight_layout #macht irgendwas schoener. einfach dran machen...

plt.xscale("log")
plt.xlabel(r"$\nu / \nu_0 $")
plt.ylabel(r"$U_B/U_S$")


plt.tight_layout
plt.legend(loc="best")

plt.savefig('plotFrequenz.pdf')
