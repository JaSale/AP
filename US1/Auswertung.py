import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import stats

#Messung der Schallgeschwindigkeit in Acryl
t1_1 = 30.4*10**(-6) #Sekunden
U1_1 = 1.3 #Volt
t1_2 = 60.0*10**(-6) #Sekunden
U1_2 = 0.139 #Bolt
s_1 = ufloat(4.025*10**(-2), 0.005*10**(-2))
c1_Acryl = 2*s_1/(t1_2-t1_1)
print('c1_Acryl: ', c1_Acryl)

#Berechnung der Dämpfung

A2_1, t2_1, A2_2, t2_2, l = np.genfromtxt('Dämpfung.txt', unpack = True)
s = 2*l*10**(-2)

L1plot = np.linspace(0, 0.25)
def f1(s, a, U_0):
    return U_0*np.exp(-a*s)
paramsI, covarianceI = curve_fit(f1, s, A2_2)
errorsI = np.sqrt(np.diag(covarianceI))
U_0 = ufloat(paramsI[1], errorsI[1])
a = ufloat(paramsI[0], errorsI[0])

print('U_0: ', U_0)
print('a: ', a)

#Schallgeschwindigkeit: Impuls-Echo-Verfahren
deltat3 = (t2_2 - t2_1)/2

L1plot = np.linspace(0, 50)
def f1(deltat3, c, b):
    return deltat3 * c +b
paramsI, covarianceI = curve_fit(f1, deltat3, l)
errorsI = np.sqrt(np.diag(covarianceI))
b = ufloat(paramsI[1], errorsI[1])
c = ufloat(paramsI[0], errorsI[0])
print('Impuls-Echo-Verfahren')
print('b: ', b)
print('c-Acryl: ', c)

#Schallgeschwindigkeit: Dursschall-Verfahren
t, l = np.genfromtxt('Durchschall-Verfahren.txt', unpack=True)

L1plot = np.linspace(0, 50)
def f1(t, c, b):
    return t * c +b
paramsI, covarianceI = curve_fit(f1, t, l)
errorsI = np.sqrt(np.diag(covarianceI))
b = ufloat(paramsI[1], errorsI[1])
c = ufloat(paramsI[0], errorsI[0])
print('Durchschall-Verfahren:')
print('b: ', b)
print('c-Acryl: ', c)


#Augenmodel
c_GK = 1410
c_L = 2500
#Außen-Iris
deltat1= (11.3-0.4)/2*10**(-6)
l1= deltat1*c_GK*10**3
#Iris-Linse
deltat2= (17.1-11.3)/2*10**(-6)
l2= deltat2*c_GK*10**3
#Linse
deltat3 = (23.6-17.1)/2*10**(-6)
l3 = deltat3*c_L*10**3
#Glaskörper
deltat4 = (73.2-23.6)/2*10**(-6)
l4 = deltat4*c_GK*10**3

print('l1:', l1)
print('l2:', l2)
print('l3:', l3)
print('l4:', l4)
