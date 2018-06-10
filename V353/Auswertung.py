#alle benoetigten pakete laden
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import stats
import pylab
Figure = pylab.figure()
Ax = Figure.gca


#Aufgbenteil A)
x, y = np.genfromtxt('A.txt', unpack=True)
y= (y +1020)*10**(-3) # y verschieben
x = (x + 5.500)*10**(-3) # x verschieben

def f(x, m, b):
    return m*x+b
paramsI, covarianceI = curve_fit(f, x, np.log(y))
errorsI = np.sqrt(np.diag(covarianceI))
b = ufloat(paramsI[1], errorsI[1])
m = ufloat(paramsI[0], errorsI[0])

z = -1 * 1/m
print(m)
print(b)
print('RC1 =')
print(z)

#AUfgabenteil B)
x, y = np.genfromtxt('B.txt', unpack=True)
U = 960
y = y/U

def f(x, a):
    return 1/np.sqrt(1+(2*np.pi*x*a)**2)
paramsI, covarianceI = curve_fit(f, x, y)
errorsI = np.sqrt(np.diag(covarianceI))
a = ufloat(paramsI[0], errorsI[0])
print('RC2 =')
print(a)

#Aufgabenteil C)
x, c, d = np.genfromtxt('C.txt', unpack=True)
y = c/d*2*np.pi*10**(-3)

def f(x, e):
    return np.arctan(-2*np.pi*x*e)
paramsI, covarianceI = curve_fit(f, x, y)
errorsI = np.sqrt(np.diag(covarianceI))

e = ufloat(paramsI[0], errorsI[0])
print('RC3 =')
print(e)
