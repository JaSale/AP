import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import stats
# c ist die spzifische Wärmekapazität
# C ist die Molwärme

# Bestimmung von cgmg____________________________________________________
#hier werden die Werte eingetragen, die du im ersten Teil des Versuchs misst
m_x = 287.00 # Masse von Wassermenge des kalten Wassers
m_y = 274.55 # Masse von Wassermenge des heißen Wassers
T_x = 22.5 # Temperatur, kaltes Wasser
T_y = 98.9 # Temperatur, warmes Wasser
T_m = 58.7 # mittlere Temperatur, also von dem gemischten Wasser
cw = 4.18 #fester wert

cgmg = (cw * m_y * (T_y - T_m) - cw * m_x * (T_m - T_x)) / (T_m - T_x)

print ('cgmg = ', cgmg)

#hier werden die Massen von  G (Graphit), Z (Zinn) und A (Aluminium) eingelesen und die dazugehörigen Massen des Wasser, in der du die Metalle kühlst
m_G = 105.45
m_Z = 203.77
m_A = 112.91
m_G_Wasser = 670.59
m_Z_Wasser = 665.88
m_A_Wasser = 665.88



#Graphit_______________________________________________________________________________
print('Graphit:')
#Messung1
T_G1_Wasser = 23.5 #Temperatur der 1. Messung von dem Wasser
T_G1_Metall = 53.1 #Temperatur der 2. Messung von dem Metall
T_G1_Mittel = 25.0 #Temperatur, nachdem du das Metall ins Wasser gelegt hast und man sowohl am Metall als auch im Wasser die gleiche Temperatur misst.

T_G2_Wasser = 24.9 #hier analog zu vorher, nur Messung 2
T_G2_Metall = 50.2
T_G2_Mittel = 26.9

T_G3_Wasser = 26.7 # analog wie oben: Messung 3
T_G3_Metall = 54.3
T_G3_Mittel = 28.9
# ab hier sind die Rechnungen für die spezifischen Wärmekapazitäten ("im Terminal: kleines c")
c_G1 = (cw * m_G_Wasser + cgmg) * (T_G1_Mittel - T_G1_Wasser) / (m_G * (T_G1_Metall - T_G1_Mittel))
print ('c_G1 = ', c_G1) # hier werden die dir einfach nur im Terminal ausgespuckt
c_G2 = (cw * m_G_Wasser + cgmg) * (T_G2_Mittel - T_G2_Wasser) / (m_G * (T_G2_Metall - T_G2_Mittel))
print ('c_G2 = ', c_G2)
c_G3 = (cw * m_G_Wasser + cgmg) * (T_G3_Mittel - T_G3_Wasser) / (m_G * (T_G3_Metall - T_G3_Mittel))
print ('c_G3 = ', c_G3)

c_Gmean = np.array([c_G1, c_G2, c_G3]) # hier werden die Werte c_G1, c_G2 und c_G3 in ein array geschrieben
c_G= ufloat(np.mean(c_Gmean), stats.sem(c_Gmean)) # hier wird dir automatisch der Mittelwert + Fehler des arrays berechnet
#np.mean = Mittelwert bilden
#stats.sem = Standardabweichung
print('c_G = ' , c_G)

#folgend sind einfach nur die Werte aus der Tabelle (aus der Anleitung) die musst du ggf. nochmal für dich ändern, falls in ein anderes Metall habt
M_G = 12.0 # fester Wert für ein Metall
a_G = 8 * 10**(-6) # fester Wert für ein Metall -> in der Tabelle: ALPHA
k_G = 33 * 10**9 # fester Wert für ein Metall
p_k = 2.25 * 10**6 # fester Wert für ein Metall -> in der Tabelle: RHO

#hier drunter wird die Molwärme C für jede einzelne Messung berechnet
C_G1 = c_G1 * M_G - 9 * a_G**2 *  k_G * M_G * (T_G1_Mittel + 273) / p_k
C_G2 = c_G2 * M_G - 9 * a_G**2 *  k_G * M_G * (T_G2_Mittel + 273) / p_k
C_G3 = c_G3 * M_G - 9 * a_G**2 *  k_G * M_G * (T_G3_Mittel + 273) / p_k
print('C_G1 = ' , C_G1)
print('C_G2 = ' , C_G2)
print('C_G2 = ' , C_G3)
#hier drunter wird einfach wieder wie oben ein Array erzeugt mit den Werten und daraus der Mittelwert und der Fehler berechnet
C_Gmean = np.array([C_G1, C_G2, C_G3])
C_G= ufloat(np.mean(C_Gmean), stats.sem(C_Gmean))
print('C_G =', C_G)
#hier hab ich den Mittelwert und den Fehler noch einmal per Hand berechnet, da mir der oben drüber zu ungenau war
C_G = (C_G1 + C_G2 + C_G3)/3 # Mittelwert
C_GF = (((C_G1 - C_G)**2 + (C_G2-C_G)**2 + (C_G3-C_G)**2)/(2*3))**(1/2) # Fehler
print('C_G = ' , C_G , ' +-', C_GF)

#Zinn___________________________________________________________________________________________
print('Zinn:')
#hier werden wie oben die Temperaturen, die ihr gemessen habt, eingetragen
T_Z1_Wasser = 22.2
T_Z1_Metall = 56.3
T_Z1_Mittel = 23.4

T_Z2_Wasser = 25.8
T_Z2_Metall = 50.8
T_Z2_Mittel = 27.1

T_Z3_Wasser = 27.0
T_Z3_Metall = 63.2
T_Z3_Mittel = 28.1
#Berechnung der spezifischen Wärmekapazität
c_Z1 = (cw * m_Z_Wasser + cgmg) * (T_Z1_Mittel - T_Z1_Wasser) / (m_Z * (T_Z1_Metall - T_Z1_Mittel))
print ('c_Z1 = ', c_Z1)
c_Z2 = (cw * m_Z_Wasser + cgmg) * (T_Z2_Mittel - T_Z2_Wasser) / (m_Z * (T_Z2_Metall - T_Z2_Mittel))
print ('c_Z2 = ', c_Z2)
c_Z3 = (cw * m_Z_Wasser + cgmg) * (T_Z3_Mittel - T_Z3_Wasser) / (m_Z * (T_Z3_Metall - T_Z3_Mittel))
print ('c_Z3 = ', c_Z3)
#Mittelwert und Standardabweichung
c_Zmean = np.array([c_Z1, c_Z2, c_Z3])
c_Z= ufloat(np.mean(c_Zmean), stats.sem(c_Zmean))
print('c_Z =', c_Z)
#Werte aus der Tabelle (Anleitung)
M_Z = 118.7
a_Z = 27 * 10**(-6)
k_Z = 55 * 10**9
p_Z = 7.28 * 10**6
#Berechnung der Molwärme
C_Z1 = c_Z1 * M_Z - 9 * a_Z**2 *  k_Z * M_Z * (T_Z1_Mittel + 273) / p_Z
C_Z2 = c_Z2 * M_Z - 9 * a_Z**2 *  k_Z * M_Z * (T_Z2_Mittel + 273) / p_Z
C_Z3 = c_Z3 * M_Z - 9 * a_Z**2 *  k_Z * M_Z * (T_Z3_Mittel + 273) / p_Z
print('C_Z1 = ' , C_Z1)
print('C_Z2 = ' , C_Z2)
print('C_Z3 = ' , C_Z3)
#Mittelwert und Fehler
C_Zmean = np.array([C_Z1, C_Z2, C_Z3])
C_Z= ufloat(np.mean(C_Zmean), stats.sem(C_Zmean))
print('C_Z = ', C_Z)
#Mittelwert und Fehler per Hand (da mir der da drüber zu ungenau war)
C_Z = (C_Z1 + C_Z2 + C_Z3)/3
C_ZF = (((C_Z1 - C_Z)**2 + (C_Z2-C_Z)**2 + (C_Z3-C_Z)**2)/(2*3))**(1/2)
print('C_Z = ' , C_Z , ' +-', C_ZF)
#Aluminium______________________________________________________
print('Aluminium:')
#gemessene Temperaturen
T_A1_Wasser = 23.4
T_A1_Metall = 56.3
T_A1_Mittel = 25.8
#Berechnung spezifische Wärmekapazität
c_A1 = (cw * m_A_Wasser + cgmg) * (T_A1_Mittel - T_A1_Wasser) / (m_A * (T_A1_Metall - T_A1_Mittel))
print ('c_A1 = ', c_A1)
#Werte aus der Tabelle (Anleitung)
M_A = 27
a_A =23.5 * 10**(-6)
k_A = 75 * 10**9
p_A = 2.7 * 10**6
#Berechnung der Molwärme
C_A1 = c_A1 * M_A - 9 * a_A**2 *  k_A * M_A * (T_A1_Mittel + 273) / p_A
print( 'C_A1 =', C_A1)
#hier hat man kein Mittelwert oder Fehler, da man nur einen Wert errechnet
