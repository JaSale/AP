import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import stats

m_alle , Ub = np.genfromtxt('Steigungen2.txt', unpack = True)
Ub_Kehrwert_Wurzel = 1/(Ub**(1/2))
def f6(Ub_Kehrwert_Wurzel, m, n):
    return Ub_Kehrwert_Wurzel*m + n
paramsI, covarianceI = curve_fit(f6, Ub_Kehrwert_Wurzel, m_alle, sigma=[110, 50, 70, 110, 110])
errorsI = np.sqrt(np.diag(covarianceI))
n = ufloat(paramsI[1], errorsI[1])
m = ufloat(paramsI[0], errorsI[0])

L1plot = np.linspace(0.045, 0.075)
plt.plot(Ub_Kehrwert_Wurzel, m_alle,'ro', label="Messwerte")
plt.xlabel(r"$\frac{1}{\sqrt{U_b}} / \mathrm{\frac{1}{\sqrt{V}}}$")
plt.ylabel(r"$m / \mathrm{\sqrt{\frac{kC}{Vg}}}$")
#linreg
plt.plot(L1plot, f6(L1plot, *paramsI) , 'b-', label='Lineare Regression')
plt.tight_layout()
plt.legend(loc="best")

plt.savefig('PlotSteigung2.pdf')
