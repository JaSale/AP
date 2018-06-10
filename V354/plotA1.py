#alle benoetigten pakete laden
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import stats

#erstelle eine .txt Datei, aus der die Werte fuer die Funktion genommen werden koennen. Das, was in der ersten Spalte steht, sind automaisch die x-Werte,
#die zweite die y-Werte.

x, y = np.genfromtxt('a1.txt', unpack=True)
#linregress vorbereitung(Fkt definieren m=Steigung, n=y-Schnittpkt)
def f(y, a, b, c):

    return a*np.exp(-b*y)+c
paramsI, covarianceI = curve_fit(f, x, y, p0=[1,1,-0.6])#das muss hier einfach alles hin...kann nicht genau sagen, was es macht.
errorsI = np.sqrt(np.diag(covarianceI))
b = ufloat(paramsI[1], errorsI[1])
a = ufloat(paramsI[0], errorsI[0])
c = ufloat(paramsI[2], errorsI[2])
print(a, b/(2*np.pi), c) #Dieser Befehl gibt euch in der Kommandozeile als ersten Wert fuer m mit Fehler und den zweiten Wert
#fuer n wieder mit Fehler.


#with plt.xkcd(): (macht, dass die ganze Sache in comic sans ms optik ausgegeben wird. Sieht sehr fein aus, ist aber vielleicht nicht sooo wichtig)
#Plot der Messwerte:

L1plot = np.linspace(-6, 460)#Grenzen fuer linregr. guckt nach den Grenzwerten fuer die x-Werte.
#plt.xlim(-7, 450)
#plt.ylim(-6, 1)
plt.plot(x, y,'r*', label="Messwerte") #r+, macht, dass eure Werte als rote Plusse erscheinen. mit b* kommen blaue sterne...mehr Farben kann man online finden;)
#Achsen beschriften!!!!!!
plt.ylabel(r"$U / \mathrm{V} $") #hier wurde Tex Code verwendet, um Brueche ordentlich darzustellen. das T_P macht, dass das P als Indesx von T erscheint. Hinter den Slash kommt die Einheit fuer die jeweilige Groesse
plt.xlabel(r"$ t / \mathrm{\mu s}$")
plt.plot(L1plot, f(L1plot, *paramsI) , 'b-', label='exponentielle Regression') #b- macht eine blaue durchgezogene Linie
plt.tight_layout #macht irgendwas schoener. einfach dran machen...
plt.legend(loc="best") #macht die Legende an den Ort innerhalb des Plots, wo am meisten Platz dafuer ist.

#plt.show()
plt.savefig('plotA1.pdf') #erstellt und speichert automatisch den Plot als pdf datei
