import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import stats


A11, A12, t1, A21, A22, t2 = np.genfromtxt('KappaEdelstahl.txt' , unpack=True)
A1=A12-A11
A2=A22-A21
t= 2* (t2 - t1)

print('A1', A1)
print('A2', A2)
print('t', t)
