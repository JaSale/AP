from uncertainties import ufloat
import numpy as np
import uncertainties.unumpy as unp
import scipy.constants as sp
import math
p =  ufloat(1.04772115 , 0.00017453)
#p=(p*2*np.pi)/360
       #Größe mit Fehler hinter dem Komma
#e = 1.602*10**(-19)
#a = ufloat (0.00000000735 , 0.00000000014)

#po = 1.0132

T =  (unp.sin( ( p  + (62.6*2*np.pi/360) ) /2))/unp.sin( p /2)#Wenn fehlerbehaftete Größe in Funktion (sin, cos, sqrt, etc unp.... und nicht np.)

print (T)
