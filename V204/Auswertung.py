import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import stats


Z, T_1, T_2, T_3, T_4, T_5, T_6, T_7, T_8 = np.genfromtxt('Messung1.txt' , unpack=True)
t = Z

print('Nach 700 Sekunden:')
print('T1', 33.64 )
print('T4', 32.51 )
print('T5', 36.81 )
print('T8', 26.95 )

#Messing
A= 1.2*0.4*10**(-4)
k= 120 #Literaturwert, Einheit: W/(mK)
dT=0
dx=3*10**(-2)
#Q_durch_t = -k*A*dT/dx

#Kappa Messing ______________________________________________________________________
A_M_fern, A_M_nah, dt_M = np.genfromtxt('KappaMessing.txt', unpack = True)
rho_M = 8520
c_M = 385
T_M = 80

Kappa_M = (rho_M * c_M * dx**2)/(2*dt_M* np.log(A_M_nah/A_M_fern))

Kappa_M_mean = ufloat(np.mean(Kappa_M), stats.sem(Kappa_M))

print(Kappa_M)
print('Kappa_M:', Kappa_M_mean)

l_M = (4 * np.pi * Kappa_M_mean * T_M / (rho_M * c_M ))**(1/2)
print('l:_M ', l_M)
#Kappa Aluminium ______________________________________________________________________
A_A_fern, A_A_nah, dt_A = np.genfromtxt('KappaAluminium.txt', unpack = True)
rho_A = 2800
c_A = 830

Kappa_A = (rho_A * c_A * dx**2)/(2*dt_A* np.log(A_A_nah/A_A_fern))
print(Kappa_A)
Kappa_A_mean = ufloat(np.mean(Kappa_A), stats.sem(Kappa_A))

print('Kappa_A:', Kappa_A_mean)

l_A = (4 * np.pi * Kappa_A_mean * T_M / (rho_A * c_A ))**(1/2)
print('l_A :', l_A)
#Kappa Edelstahl______________________________________________________________________
A_E_nah, A_E_fern, dt_E = np.genfromtxt('KappaEdelstahl.txt', unpack = True)
rho_E = 8000
c_E = 400
T_E=200
Kappa_E = (rho_E * c_E * dx**2)/(2*dt_E* np.log(A_E_nah/A_E_fern))
print(Kappa_E)
Kappa_E_mean = ufloat(np.mean(Kappa_E), stats.sem(Kappa_E))

print('Kappa_E:', Kappa_E_mean)
l_E = (4 * np.pi * Kappa_E_mean * T_E / (rho_E * c_E ))**(1/2)
print('l_E :', l_E)
