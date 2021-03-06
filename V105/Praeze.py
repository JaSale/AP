import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import stats

y, x = np.genfromtxt('Praeze.txt' , unpack=True)
#linregress vorbereitung(Fkt definieren m=Steigung, n=y-Schnittpkt)
def f(x, m, n):
    return x*m + n
paramsI, covarianceI = curve_fit(f, x, y)
errorsI = np.sqrt(np.diag(covarianceI))
n = ufloat(paramsI[1], errorsI[1])
m = ufloat(paramsI[0], errorsI[0])
print(m, n)


#with plt.xkcd(): (macht, dass die ganze Sache in comic sans ms optik ausgegeben wird)
#Plot der Messwerte
L1plot = np.linspace(0, 6) #Grenzen fuer linregr.
#plt.title('Plot Gravitationsmethode')
plt.plot(x, y,'r+', label="Messwerte")
plt.ylabel(r"$\frac{1}{T_P} / \mathrm{\frac{1}{s}}$")
plt.xlabel(r"$ B / \mathrm{mT}$")
#linreg
plt.plot(L1plot, f(L1plot, *paramsI) , 'b-', label='Lineare Regression')
plt.tight_layout
plt.legend(loc="best")

plt.savefig('Praeze.pdf')
