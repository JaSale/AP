import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import stats



#linreg fuer Oszillation
y,x = np.genfromtxt('Oszi.txt' , unpack=True)
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
L1plot = np.linspace(200, 1250) #Grenzen fuer linregr.
#plt.title('Plot Methode: harmonischer Oszillator')
plt.plot(x, y,'r+', label="Messwerte")
plt.xlabel(r"$\frac{1}{B} / \mathrm{\frac{1}{T}}$")
plt.ylabel(r"$ T^2 / \mathrm{s^2}$")
#linreg
plt.plot(L1plot, f(L1plot, *paramsI) , 'b-', label='Lineare Regression')
plt.tight_layout
plt.legend(loc="best")

    #plt.ylim( 5 , 21 )
    #plt.xlim( 1 , 8 )
plt.savefig('Oszi.pdf') #Macht, dass alles als pdf gespecihert wird und erstellt eine Datei
