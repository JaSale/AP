import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import stats

Ud1 , D1_in_Zoll = np.genfromtxt('Messung1.1.txt' , unpack=True)
Ud2 , D2_in_Zoll = np.genfromtxt('Messung1.2.txt' , unpack=True)
Ud3 , D3_in_Zoll = np.genfromtxt('Messung1.3.txt' , unpack=True)
Ud4 , D4_in_Zoll = np.genfromtxt('Messung1.4.txt' , unpack=True)
Ud5 , D5_in_Zoll = np.genfromtxt('Messung1.5.txt' , unpack=True)

#umrechnen in meter
D1 = D1_in_Zoll * 0.0254 *2/8
D2 = D2_in_Zoll * 0.0254 *2/8
D3 = D3_in_Zoll * 0.0254 *2/8
D4 = D4_in_Zoll * 0.0254 *2/8
D5 = D5_in_Zoll * 0.0254 *2/8

plt.plot(Ud2, D2,'bo', label="Messwerte")

def f2(Ud2, m2 , n2):
    return m2 * Ud2 +n2
paramsI, covarianceI = curve_fit(f2, Ud2, D2)
errorsI = np.sqrt(np.diag(covarianceI))
m2 = ufloat(paramsI[0], errorsI[0])
n2 = ufloat(paramsI[1], errorsI[1])

L1plot = np.linspace(-16, 36)
plt.plot(L1plot, f2(L1plot, *paramsI) , 'g-', label ="Lineare Regression")
plt.xlabel(r"$U_d / \mathrm{V}$")
plt.ylabel(r"$D / \mathrm{m}$")
plt.tight_layout()
plt.legend(loc="best")
plt.savefig('Plot1.2.pdf')
