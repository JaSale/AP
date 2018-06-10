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
#erstelle eine .txt Datei, aus der die Werte fuer die Funktion genommen werden koennen. Das, was in der ersten Spalte steht, sind automaisch die x-Werte,
#die zweite die y-Werte.

x, y = np.genfromtxt('c.txt', unpack=True)
y = y*10
#linregress vorbereitung(Fkt definieren m=Steigung, n=y-Schnittpkt)
def f(x, a, b, c):
    return a*np.exp(-b*x)+c
paramsI, covarianceI = curve_fit(f, x, y)#das muss hier einfach alles hin...kann nicht genau sagen, was es macht.
errorsI = np.sqrt(np.diag(covarianceI))
b = ufloat(paramsI[1], errorsI[1])
a = ufloat(paramsI[0], errorsI[0])
c = ufloat(paramsI[2], errorsI[2])
print(a,b, c) #Dieser Befehl gibt euch in der Kommandozeile als ersten Wert fuer m mit Fehler und den zweiten Wert
#fuer n wieder mit Fehler.


#with plt.xkcd(): (macht, dass die ganze Sache in comic sans ms optik ausgegeben wird. Sieht sehr fein aus, ist aber vielleicht nicht sooo wichtig)
#Plot der Messwerte:
#plt.xscale("log")
#plt.yscale("log")
xposition = [31.2, 40.4]
for xc in xposition:
    plt.axvline(x=xc, color='g', linestyle=':', label=r"±$\nu$")

xposition = [36]
for xc in xposition:
    plt.axvline(x=xc, color='b', linestyle=':', label='Resonanzüberhöhung')

yposition = [2.250]
for yc in yposition:
    plt.axhline(y=yc, color='y', linestyle=':', label='Resonanzbreite')
L1plot = np.linspace(0, 0)#Grenzen fuer linregr. guckt nach den Grenzwerten fuer die x-Werte.
plt.xlim(13, 61)
plt.ylim(0, 3)
plt.plot(x, y,'r*', label="Messwerte") #r+, macht, dass eure Werte als rote Plusse erscheinen. mit b* kommen blaue sterne...mehr Farben kann man online finden;)
#Achsen beschriften!!!!!!
plt.ylabel(r"$ \frac{U_C}{U_0} / \mathrm{V}$" ) #hier wurde Tex Code verwendet, um Brueche ordentlich darzustellen. das T_P macht, dass das P als Indesx von T erscheint. Hinter den Slash kommt die Einheit fuer die jeweilige Groesse
plt.xlabel(r"$ ln(\nu) / \frac{1}{s} $")
plt.plot(L1plot, f(L1plot, *paramsI)) #b- macht eine blaue durchgezogene Linie
plt.tight_layout #macht irgendwas schoener. einfach dran machen...
plt.legend(loc="best") #macht die Legende an den Ort innerhalb des Plots, wo am meisten Platz dafuer ist.

#plt.show()
plt.savefig('plotC2.pdf') #er
