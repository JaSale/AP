#alle benoetigten pakete laden
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import stats

#erstelle eine .txt Datei, aus der die Werte fuer die Funktion genommen werden koennen. Das, was in der ersten Spalte steht, sind automaisch die x-Werte,
#die zweite die y-Werte.

x, y = np.genfromtxt('a.txt' , unpack=True)
y=y**2
#linregress vorbereitung(Fkt definieren m=Steigung, n=y-Schnittpkt)
L1plot = np.linspace(390, 700)
def f(x, ao, ai):
    return ao + ai/(x**2)
paramsI, covarianceI = curve_fit(f, x[:6], y[:6])#das muss hier einfach alles hin...kann nicht genau sagen, was es macht.
errorsI = np.sqrt(np.diag(covarianceI))
ao = ufloat(paramsI[1], errorsI[1])
ai = ufloat(paramsI[0], errorsI[0])
plt.plot(L1plot, f(L1plot, *paramsI) , 'b-', label='Theoriekurve_1')
print(ao, ai) #Dieser Befehl gibt euch in der Kommandozeile als ersten Wert fuer m mit Fehler und den zweiten Wert
#fuer n wieder mit Fehler.

#def f1(x, o, u):
#    return o + u/(x**2)
#paramsI, covarianceI = curve_fit(f1, x, y)#das muss hier einfach alles hin...kann nicht genau sagen, was es macht.
#errorsI = np.sqrt(np.diag(covarianceI))
#o = ufloat(paramsI[1], errorsI[1])
#u = ufloat(paramsI[0], errorsI[0])
#plt.plot(L1plot, f1(L1plot, *paramsI) , 'b--', label='Theoriekurve_1.2')

def g(x, a, i):
    return a*x**2+i
paramsI, covarianceI = curve_fit(g, x, y)#das muss hier einfach alles hin...kann nicht genau sagen, was es macht.
errorsI = np.sqrt(np.diag(covarianceI))
a = ufloat(paramsI[1], errorsI[1])
i = ufloat(paramsI[0], errorsI[0])
print(a, i)

#with plt.xkcd(): (macht, dass die ganze Sache in comic sans ms optik ausgegeben wird. Sieht sehr fein aus, ist aber vielleicht nicht sooo wichtig)
#Plot der Messwerte:

 #Grenzen fuer linregr. guckt nach den Grenzwerten fuer die x-Werte.
plt.title('Plot Dispersionskurve') #Ueberschrift, die ueber dem PLot stehen wird
plt.plot(x, y,'r+', label="Messwerte") #r+, macht, dass eure Werte als rote Plusse erscheinen. mit b* kommen blaue sterne...mehr Farben kann man online finden;)
#Achsen beschriften!!!!!!
plt.ylabel(r"$n^2$") #hier wurde Tex Code verwendet, um Brueche ordentlich darzustellen. das T_P macht, dass das P als Indesx von T erscheint. Hinter den Slash kommt die Einheit fuer die jeweilige Groesse
plt.xlabel(r"$ \lambda / nm$")

plt.plot(L1plot, g(L1plot, *paramsI) , 'g-.', label='Theoriekurve_2') #b- macht eine blaue durchgezogene Linie
plt.tight_layout #macht irgendwas schoener. einfach dran machen...
plt.legend(loc="best") #macht die Legende an den Ort innerhalb des Plots, wo am meisten Platz dafuer ist.

plt.savefig('dispersion.pdf')
