import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import *


def f(Xneu,c,d):
    return c*Xneu+d

V1,U1=np.genfromtxt('Quotienten.txt', unpack=True)
U=24
Uc1=U1/U
x1=np.linspace(15,37.8,100)
x2=np.linspace(37.84,50,100)
w1=2*np.pi*x1*10**3
w2=2*np.pi*x2*10**3
R=271.6
L=3.53*10**(-3)
C=5.015*10**(-9)
Uv1=1/(np.sqrt((1-L*C*w1**2)**2+w1**2*R**2*C**2))
Uv2=1/(np.sqrt((1-L*C*w2**2)**2+w2**2*R**2*C**2))

V2,U2=np.genfromtxt('Quotienten.txt', unpack=True)
U=24
Uc2=U2/U

plt.figure(1)
plt.subplot(211)
#plt.plot((32.196, 32.196), (1.5, 3.0), 'g--', label='Resonanzbreite')
#plt.plot((44.442, 44.442), (1.5, 3.0), 'g--')
plt.plot(x1,Uv1,'b-', label='Theoriekurve')
plt.plot(x2,Uv2,'b-')
plt.plot(V1,Uc1, 'rx', label='Messwerte')
plt.ylabel(r'$\frac{U_{C}}{U}$')
plt.legend(loc='best')
plt.savefig('Quotienten.pdf')
plt.show()