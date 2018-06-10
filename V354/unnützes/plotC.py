#alle benoetigten pakete laden
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import stats
import pylab

#Firgure = pylab.figure()
#Ax = Figure.gca()
#erstelle eine .txt Datei, aus der die Werte fuer die Funktion genommen werden koennen. Das, was in der ersten Spalte steht, sind automaisch die x-Werte,
#die zweite die y-Werte.

y, x = np.genfromtxt('c.txt' , unpack=True)



#with plt.xkcd(): (macht, dass die ganze Sache in comic sans ms optik ausgegeben wird. Sieht sehr fein aus, ist aber vielleicht nicht sooo wichtig)
#Plot der Messwerte:
#Ax.set_xscale("log")
#Ax.set_yscale("log")
plt.xlim(10, 65)
plt.ylim(0, 0.5)
plt.title('Plot Schwingungsamplituden') #Ueberschrift, die ueber dem PLot stehen wird
plt.plot(x, y,'r+', label="Messwerte") #r+, macht, dass eure Werte als rote Plusse erscheinen. mit b* kommen blaue sterne...mehr Farben kann man online finden;)
#Achsen beschriften!!!!!!
#plt.ylabel(r"$\frac{1}{T_P} / \frac{1}{s}$") #hier wurde Tex Code verwendet, um Brueche ordentlich darzustellen. das T_P macht, dass das P als Indesx von T erscheint. Hinter den Slash kommt die Einheit fuer die jeweilige Groesse
#plt.xlabel(r"$ B / mT$")
#plt.plot(L1plot, f(L1plot, *paramsI) , 'b-', label='Regression') #b- macht eine blaue durchgezogene Linie
plt.tight_layout #macht irgendwas schoener. einfach dran machen...
plt.legend(loc="best") #macht die Legende an den Ort innerhalb des Plots, wo am meisten Platz dafuer ist.

plt.savefig('plotC.pdf') #erstellt und speichert automatisch den Plot als pdf datei
