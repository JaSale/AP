from uncertainties import ufloat
import numpy as np
import uncertainties.unumpy as unp
import scipy.constants as sp
import math
ai =  ufloat(50500 , 1300)
ao =  ufloat(2.812 , 0.005)
C=656
D=589
F=486


#p=(p*2*np.pi)/360
       #Größe mit Fehler hinter dem Komma
#e = 1.602*10**(-19)
#a = ufloat (0.00000000735 , 0.00000000014)

#po = 1.0132

T =  (ai/(ao-1))**(0.5)
print (T)
