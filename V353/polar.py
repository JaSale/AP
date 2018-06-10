import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp

f, b, a = np.genfromtxt('C.txt', unpack=True)
#f Frequenz
#b Periodendauer
#a Zeitdifferenz
r, A= np.genfromtxt('B.txt', unpack=True)
#r ist unnütz
#A ist die Ammplitude der Kondensatorspannung
# 960 ist die Spannung des Generators
B = A / 960
phi = (a / b) * 360



#-----------------------------------------------
def H(x, c):
    return -np.sin(c)/x
paramsI, covarianceI = curve_fit(f, x, y)#das muss hier einfach alles hin...kann nicht genau sagen, was es macht.
errorsI = np.sqrt(np.diag(covarianceI))

plt.polar(phi, B, 'rx')
L = np.linspace(0.0000001, 1)
plt.polar(L, f(*paramsI, L), 'b-')
plt.savefig('buildpolar.pdf')
plt.clf()
