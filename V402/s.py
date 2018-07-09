from uncertainties import ufloat
import numpy as np
import uncertainties.unumpy as unp
import scipy.constants as sp
import math
ai =  ufloat(0.00000058 , 0.00000005)
ao =  ufloat(3.165 , 0.014)
g=1.71383
f=1.72097
e=1.72627
d=1.73414
c=1.74189
b=1.74446
a=1.75375

gg=643.84
ff=576.96
ee=546.07
dd=508.58
cc=479.99
bb=467.81
aa=435.83
#p=(p*2*np.pi)/360
       #Größe mit Fehler hinter dem Komma
#e = 1.602*10**(-19)
#a = ufloat (0.00000000735 , 0.00000000014)

#po = 1.0132

T =  (1/5)*( (a**2 - ao + ai*(aa**2))**2 +  (b**2 - ao + ai*(bb**2))**2 + (c**2 - ao +ai*(cc**2))**2 + (d**2 - ao + ai*(dd**2))**2 + (e**2 - ao + ai*(ee**2))**2 +(f**2 - ao + ai*(ff**2))**2 +(g**2 - ao + ai*(gg**2))**2)
print (T)
