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

x, y = np.genfromtxt('A.txt', unpack=True)
y= y +1020 # y verschieben und logarithmieren
x = x + 5.500 # x verschieben
#linregress vorbereitung(Fkt definieren m=Steigung, n=y-Schnittpkt)
def f(x, m, b):
    return m*x+b
paramsI, covarianceI = curve_fit(f, x, np.log(y))#das muss hier einfach alles hin...kann nicht genau sagen, was es macht.
errorsI = np.sqrt(np.diag(covarianceI))
b = ufloat(paramsI[1], errorsI[1])
m = ufloat(paramsI[0], errorsI[0])
print(m, b) #Dieser Befehl gibt euch in der Kommandozeile als ersten Wert fuer m mit Fehler und den zweiten Wert
#fuer n wieder mit Fehler.


#with plt.xkcd(): (macht, dass die ganze Sache in comic sans ms optik ausgegeben wird. Sieht sehr fein aus, ist aber vielleicht nicht sooo wichtig)
#Plot der Messwerte:
#plt.yscale("log")
L1plot = np.linspace(0, 3)#Grenzen fuer linregr. guckt nach den Grenzwerten fuer die x-Werte.
#plt.xlim(0, 3)
#plt.ylim(0, )
plt.plot(x, np.log(y),'r*', label="Messwerte") #r+, macht, dass eure Werte als rote Plusse erscheinen. mit b* kommen blaue sterne...mehr Farben kann man online finden;)
#Achsen beschriften!!!!!!
plt.ylabel(r"$ln(U/U_0)$" ) #hier wurde Tex Code verwendet, um Brueche ordentlich darzustellen. das T_P macht, dass das P als Indesx von T erscheint. Hinter den Slash kommt die Einheit fuer die jeweilige Groesse
plt.xlabel(r"$ t / \mathrm{ms}$")
plt.plot(L1plot, f(L1plot, *paramsI) , 'b-', label='lineare Regression') #b- macht eine blaue durchgezogene Linie
plt.tight_layout #macht irgendwas schoener. einfach dran machen...
plt.legend(loc="best") #macht die Legende an den Ort innerhalb des Plots, wo am meisten Platz dafuer ist.

#plt.show()
plt.savefig('plotA.pdf') #erstellt und speichert automatisch den Plot als pdf datei
