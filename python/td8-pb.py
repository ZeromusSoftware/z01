# Probleme

import numpy as np
import matplotlib.pyplot as plt

T = [0,7,18,27,37,56,102]
C = [34.83,32.14,28.47,25.74,23.14,18.54,11.04]

def m(l):
	S = 0
	for i in range(1,7):
		S += (C[i] - C[0] * np.exp(-l * T[i])) ** 2
	return S

X = np.linspace(0,0.1,100)

Y = m(X)
plt.plot(X,Y)
plt.show()
