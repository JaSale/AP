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
#hier werden die Werte eingelesen: Druck, Counts, Channel, impulses detectet
p2, N2, C2, N2_g = np.genfromtxt('Messung2.txt', unpack=True)
N3 = np.genfromtxt('Messung3.txt', unpack=True)

#Plot1a x:Reichweite y:Zählrate____________________________________________________
plt.figure(1)
x1_0 = 2 #Abstand der Quelle und des Detektors (vielleicht ändern)
p_0= 1013.25

x1 = x1_0 * p1/p_0
r1=N1_g/120 #120 ist das Zeitintervall der Messung (vielleicht ändern)

L1plot = np.linspace(1.25, 2) #musst du nur noch anpassen
def f1(x1, s1, b1):
    return x1*s1+b1
paramsI, covarianceI = curve_fit(f1, x1[15:], r1[15:]) #hier wird durch die eckige Klammer nur ein Teil der Werte genommen (von Wert 15 bis Ende)
errorsI = np.sqrt(np.diag(covarianceI))
b1 = ufloat(paramsI[1], errorsI[1])
s1 = ufloat(paramsI[0], errorsI[0])
print('Steigung und y-Achsenabschnitt')
print(s1)
print(b1)

plt.plot(L1plot, f1(L1plot, *paramsI) , 'g-', label="Lineare Regression")
plt.plot(x1, r1, 'b.', label = 'Messwerte')
plt.xlabel(r"$x / \mathrm{cm}$")
plt.ylabel(r"$R / \mathrm{\frac{1}{s}}$")
plt.axhline(y=328.95, color='g', linestyle='--', label=r"$y=\frac{R(x=0)}{2}$")
plt.axvline(x=1.53, color='r', linestyle='-.' ,label=r"$R_m=1.53 \, \mathrm{cm}$")
#Werte der horizontalen und vertikalen Linie müssen angepasst werden
plt.tight_layout()
plt.legend(loc="best")
plt.savefig('Messung1a.pdf')

EX1=(15.3/3.1)**(2/3)#Energiewert muss angepasst werden: x-Wert der vertikalen Liniee in mm (nicht cm!))
print('EX1:', EX1, 'MeV')

#Plot1b x:Druck y:Energie_________________________________________________________
plt.figure(2)
E_0=4
E1 = C1/951*E_0 #hier musst du deinen ersten Counts-wert eintagen für p=0 statt der 951
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
x2_0 = 2.5 #das muss wieder ggf angepasst werden, (Abstand Quelle-Detektor)
p_0= 1013.25

x2 = x2_0 * p2/p_0
r2=N2_g/120 #erneut das Zeitintervall 120s, muss ggf noch angepasst werden

L1plot = np.linspace(1.4, 2.15)
def f1(x2, s2, b2):
    return x2*s2+b2
paramsI, covarianceI = curve_fit(f1, x2[12:19], r2[12:19]) #hier wird wieder nur ein Teil der Werte genommen
errorsI = np.sqrt(np.diag(covarianceI))
b2 = ufloat(paramsI[1], errorsI[1])
s2 = ufloat(paramsI[0], errorsI[0])

print('Steigung und y-Achsenabschnitt')
print(s2)
print(b2)
plt.plot(L1plot, f1(L1plot, *paramsI) , 'g-', label="Lineare Regression")

plt.plot(x2, r2, 'b.', label = 'Messwerte')
plt.xlabel(r"$x / \mathrm{cm}$")
plt.ylabel(r"$R / \mathrm{\frac{1}{s}}$")
plt.axhline(y=262.54, color='g', linestyle='--', label=r"$y=\frac{R(x=0)}{2}$")
plt.axvline(x=1.73, color='r', linestyle='-.' ,label=r"$R_m=1.73 \, \mathrm{cm}$")
#Werte der horizontalen und vertikalen Linie müssen angepasst werden
plt.tight_layout()
plt.legend(loc="best")
plt.savefig('Messung2a.pdf')
EX2=(17.3/3.1)**(2/3) #Auch hier muss mittlere Reichweite angegeben werden(in mm)
print('EX2:', EX2, 'MeV')

#Histogramm mit Verteilungen
plt.figure(4)

t = np.linspace(4700, 5700) #hier musst du nur deinen Linspace und ggf die Anzahl der bins verändern
nu = sum(N3)/100
print('Mittelwert(N3): ', nu)
sigma = (sum((N3-nu)**2)/(100))**(1/2)
print('Abweichung(N3): ', sigma)
plt.hist(N3,  bins=18, normed=True, label='Messwerte')
p_p= np.random.poisson(nu, 10000)
plt.hist(p_p, bins=18, color='g', alpha=0.5, normed=True, label='Poissonverteilung')
p_n= np.random.normal(nu, sigma, 10000)
plt.hist(p_n, bins=18, color='r', alpha=0.5, normed=True, label='Normalverteilung')
plt.legend(loc="best")
plt.xlabel(r"$Counts$")
plt.ylabel(r"$p(Counts)$")
plt.savefig('Statistik.pdf')


#tabellen erstellen
#z = np.genfromtxt('zahlen.txt' , unpack=True)
#np.savetxt('Tabelle1.txt', np.column_stack([p1, N1, C1, N1_g, E1]), delimiter=' & ', newline= r' \\'+'\n', fmt='%.2f')
#np.savetxt('Tabelle2.txt', np.column_stack([p2, N2, C2, N2_g]), delimiter=' & ', newline= r' \\'+'\n', fmt='%.0f')
#np.savetxt('Tabelle3.txt', np.column_stack([z[0:25], N3[0:25], z[25:50], N3[25:50], z[0:25], N3[50:75], z[25:50], N3[75:100] ]), delimiter=' & ', newline= r' \\'+'\n', fmt='%.0f')
