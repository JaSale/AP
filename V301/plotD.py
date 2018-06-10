import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import stats

x, y = np.genfromtxt('D.txt' , unpack=True)
x=x*10**(-3)
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
L1plot = np.linspace(0.03, 0.1) #Grenzen fuer linregr.
#plt.title('Plot Gravitationsmethode')
plt.plot(x, y,'r+', label="Messwerte")
plt.xlabel(r"$I / \mathrm{A}$")
plt.ylabel(r"$U / \mathrm{V}$")
#linreg
plt.plot(L1plot, f(L1plot, *paramsI) , 'b-', label='Lineare Regression')
plt.tight_layout
plt.legend(loc="best")

plt.savefig('plotD.pdf')
