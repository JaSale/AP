import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import stats
from scipy.stats import norm
from scipy.misc import factorial
import scipy

p1, N1, C1, N1_g = np.genfromtxt('Messung1.txt', unpack=True)
p2, N2, C2, N2_g = np.genfromtxt('Messung2.txt', unpack=True)
N3 = np.genfromtxt('Messung3.txt', unpack=True)
p1linreg, N1linreg, C1linreg, N1_glinreg =np.genfromtxt('Messung1linreg.txt', unpack=True)
p2linreg, N2linreg, C2linreg, N2_glinreg =np.genfromtxt('Messung2linreg.txt', unpack=True)

#Plot1a x:Reichweite y:Zählrate____________________________________________________
plt.figure(1)
x1_0 = 2
p_0= 1013.25 #in mbar,da p auch in mbar => egal

x1 = x1_0 * p1/p_0
r1=N1_g/120

x1linreg = x1_0 *p1linreg/p_0
r1linreg=N1_glinreg/120

L1plot = np.linspace(1.25, 2)
def f1(x1linreg, s1, b1):
    return x1linreg*s1+b1
paramsI, covarianceI = curve_fit(f1, x1linreg, r1linreg)
errorsI = np.sqrt(np.diag(covarianceI))
b1 = ufloat(paramsI[1], errorsI[1])
s1 = ufloat(paramsI[0], errorsI[0])

plt.plot(L1plot, f1(L1plot, *paramsI) , 'g-', label="Lineare Regression")
plt.plot(x1, r1, 'b.', label = 'Messwerte')
plt.xlabel(r"$x / \mathrm{cm}$")
plt.ylabel(r"$R / \mathrm{\frac{1}{s}}$")
plt.axhline(y=328.95, color='g', linestyle='--', label=r"$y=\frac{R(x=0)}{2}$")
plt.axvline(x=1.53, color='r', linestyle='-.' ,label=r"$R_m=1.53 \, \mathrm{cm}$")
plt.tight_layout()
plt.legend(loc="best")
plt.savefig('Messung1a.pdf')

EX1=(15.3/3.1)**(2/3)
print('EX1:', EX1, 'MeV')

#Plot1b x:Druck y:Energie_________________________________________________________
plt.figure(2)
E_0=4 #in MeVp1 = norm.pdf(t, N3_Mittelwert, N3_Abweichung)

E1 = C1/951*E_0 #in MeV
plt.plot(p1, E1, 'b.', label='Messwerte')
L1plot = np.linspace(0, 1000)
def f1(p1, m1, n1):
    return m1*p1+n1
paramsI, covarianceI = curve_fit(f1, p1, E1)
errorsI = np.sqrt(np.diag(covarianceI))
n1 = ufloat(paramsI[1], errorsI[1])
m1 = ufloat(paramsI[0], errorsI[0])
plt.plot(L1plot, f1(L1plot, *paramsI) , 'g-', label="Lineare Regression")
plt.xlabel(r"$p / \mathrm{mbar}$")
plt.ylabel(r"$E / \mathrm{MeV}$")
plt.tight_layout()
plt.legend(loc="best")
plt.savefig('Messung1b.pdf')
print('m1: ', m1)
print('n1: ', n1)

#Plot2a x:Reichweite y:Counts_____________________________________________________
plt.figure(3)
x2_0 = 2.5
p_0= 1013.25 #in mbar,da p auch in mbar => egal

x2 = x2_0 * p2/p_0
r2=N2_g/120

x2linreg = x2_0 *p2linreg/p_0
r2linreg=N2_glinreg/120

L1plot = np.linspace(1.4, 2.1)
def f1(x2linreg, s2, b2):
    return x2linreg*s2+b2
paramsI, covarianceI = curve_fit(f1, x2linreg, r2linreg)
errorsI = np.sqrt(np.diag(covarianceI))
b2 = ufloat(paramsI[1], errorsI[1])
s2 = ufloat(paramsI[0], errorsI[0])

plt.plot(L1plot, f1(L1plot, *paramsI) , 'g-', label="Lineare Regression")

plt.plot(x2, r2, 'b.', label = 'Messwerte')
plt.xlabel(r"$x / \mathrm{cm}$")
plt.ylabel(r"$R / \mathrm{\frac{1}{s}}$")
plt.axhline(y=262.54, color='g', linestyle='--', label=r"$y=\frac{R(x=0)}{2}$")
plt.axvline(x=1.73, color='r', linestyle='-.' ,label=r"$R_m=1.73 \, \mathrm{cm}$")
plt.tight_layout()
plt.legend(loc="best")
plt.savefig('Messung2a.pdf')
EX2=(17.3/3.1)**(2/3)
print('EX2:', EX2, 'MeV')

#Histogramm mit Normalverteilung________________________________________________
plt.figure(4)

plt.hist(N3,  bins=18, normed=True)
N3_Mittelwert = sum(N3)/100
print('Mittelwert(N3): ', N3_Mittelwert)
N3_Abweichung = (sum((N3-N3_Mittelwert)**2)/100)**(1/2)
print('Abweichung(N3): ',N3_Abweichung)

t = np.linspace(4700, 5700)
p10 = norm.pdf(t, N3_Mittelwert, N3_Abweichung)
plt.plot(t, p10, 'r-')

plt.savefig('Messung3a.pdf')

#Histogramm mit Poissonverteilung_______________________________________________
plt.figure(5)
N3=N3
plt.hist(N3,  bins=18, normed=True)
N3_min= round(np.min(N3), 0)
N3_max= round(np.max(N3), 0)
l = N3_Mittelwert
t = np.linspace(N3_min, N3_max, 10000)

P= np.random.poisson(l, 10000)

#p2 = l**t/factorial(t)*np.exp(-l)
#f=(np.exp(t*(1+np.log(l/t))-l))/(np.sqrt(2*np.pi*(t+1/6)))
plt.hist(P,  bins=18, alpha=0.75, normed=True)
#plt.plot(t, P,'r-', label="Poisson")
#plt.plot(t, p2, 'r-')
plt.savefig('Messung3b.pdf')


#tabellen erstellen
z = np.genfromtxt('zahlen.txt' , unpack=True)
np.savetxt('Tabelle1.txt', np.column_stack([p1, N1, C1, N1_g, E1]), delimiter=' & ', newline= r' \\'+'\n', fmt='%.2f')
np.savetxt('Tabelle2.txt', np.column_stack([p2, N2, C2, N2_g]), delimiter=' & ', newline= r' \\'+'\n', fmt='%.0f')
np.savetxt('Tabelle3.txt', np.column_stack([z[0:25], N3[0:25], z[25:50], N3[25:50], z[0:25], N3[50:75], z[25:50], N3[75:100] ]), delimiter=' & ', newline= r' \\'+'\n', fmt='%.0f')
