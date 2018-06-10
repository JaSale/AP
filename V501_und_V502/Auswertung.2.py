import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import stats

R = 0.282
N = 20
L = 17.5 *10**(-2)

I1 , I2, I3, I5, D1 = np.genfromtxt('Messung2.1.txt', unpack = True)
I4, D2 = np.genfromtxt('Messung2.2.txt', unpack = True)

D1 = D1 * 0.0254 *2/8
D2 = D2 * 0.0254 *2/8
mu = 4 * np.pi *10**(-7)

B1 = mu * 8/(125**(1/2)) * N * I1 /R
B2 = mu * 8/(125**(1/2)) * N * I2 /R
B3 = mu * 8/(125**(1/2)) * N * I3 /R
B4 = mu * 8/(125**(1/2)) * N * I4 /R
B5 = mu * 8/(125**(1/2)) * N * I5 /R

A1 = D1 /(L**2 + D1**2)
A2 = D2 /(L**2 + D2**2)

def f1(B1, m1 , n1):
    return m1 * B1 +n1
paramsI, covarianceI = curve_fit(f1, B1,A1)
errorsI = np.sqrt(np.diag(covarianceI))
n1 = ufloat(paramsI[1], errorsI[1])
m1 = ufloat(paramsI[0], errorsI[0])
print("m1 = " , m1)

def f2(B2, m2 , n2):
    return m2 * B2 +n2
paramsI, covarianceI = curve_fit(f2, B2, A1)
errorsI = np.sqrt(np.diag(covarianceI))
n2 = ufloat(paramsI[1], errorsI[1])
m2 = ufloat(paramsI[0], errorsI[0])
print("m2 = " , m2)

def f3(B3, m3 , n3):
    return m3 * B3 +n3
paramsI, covarianceI = curve_fit(f3, B3, A1)
errorsI = np.sqrt(np.diag(covarianceI))
n3 = ufloat(paramsI[1], errorsI[1])
m3 = ufloat(paramsI[0], errorsI[0])
print("m3 = " , m3)

def f4(B4, m4 , n4):
    return m4 * B4 +n4
paramsI, covarianceI = curve_fit(f4, B4, A2)
errorsI = np.sqrt(np.diag(covarianceI))
n4 = ufloat(paramsI[1], errorsI[1])
m4 = ufloat(paramsI[0], errorsI[0])
print("m4 = " , m4)

def f5(B5, m5 , n5):
    return m5 * B5 +n5
paramsI, covarianceI = curve_fit(f5, B5, A1)
errorsI = np.sqrt(np.diag(covarianceI))
n5 = ufloat(paramsI[1], errorsI[1])
m5 = ufloat(paramsI[0], errorsI[0])
print("m5 = " , m5)



plt.figure(2)
#m_alle = np.uarray([m1, m2, m3, m4, m5])
m_alle , Ub = np.genfromtxt('Steigungen2.txt', unpack = True)
m_alle = m_alle *10**3
Ub_Kehrwert_Wurzel = 1/(Ub**(1/2))
def f6(Ub_Kehrwert_Wurzel, m, n):
    return Ub_Kehrwert_Wurzel*m + n
paramsI, covarianceI = curve_fit(f6, Ub_Kehrwert_Wurzel, m_alle, sigma=[110, 50, 70, 110, 110])
errorsI = np.sqrt(np.diag(covarianceI))
n = ufloat(paramsI[1], errorsI[1])
m = ufloat(paramsI[0], errorsI[0])
print("m, n = ", m, n)

L1plot = np.linspace(0.045, 0.075)
plt.plot(Ub_Kehrwert_Wurzel, m_alle,'ro', label="Messwerte")
plt.xlabel(r"$\frac{1}{\sqrt{U_b}} / \mathrm{\frac{1}{\sqrt{V}}}$")
plt.ylabel(r"$m / \mathrm{\sqrt{\frac{C}{Vkg}}}$")
#linreg
plt.plot(L1plot, f6(L1plot, *paramsI) , 'b-', label='Lineare Regression')
plt.tight_layout()
plt.legend(loc="best")

plt.savefig('plotSteigung2.pdf')

spezifischeLadung = 8*m**2
print("Spezifische Ladung : " ,spezifischeLadung)

I_Erdmagnetfeld = 0.195
alpha = (71 + 73 + 65)/3
alpha = ufloat(66.667, 3.205)
B_Erdmagnetfeld = mu * 8/(125**(1/2)) * N* I_Erdmagnetfeld /R
print("B = ", B_Erdmagnetfeld)
B_Erdmagnetfeld = B_Erdmagnetfeld / np.cos(69.667/360*2*np.pi)
print("B Erde = ", B_Erdmagnetfeld)
print("Alpha = ", alpha)
