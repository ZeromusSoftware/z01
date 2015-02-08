# Exercice 1

import numpy as np
import matplotlib.pyplot as plt

ecart =0.1
X = np.linspace(-np.pi/2+ecart,np.pi/2-ecart,100)
Y = np.tan(X)
plt.figure(1)
plt.clf()
plt.subplot(2,3,1)
plt.plot(X,Y)
#plt.axis([-np.pi/2,np.pi/2,-10,10])

X = np.linspace(0,10,1000)
X = X[1:]
Y = np.log(X)
plt.subplot(2,3,2)
plt.plot(X,Y)

Y = np.sin(X)/X
plt.subplot(2,3,3)
plt.plot(X,Y)

a = 2
b = 1

T = np.linspace(0,10,1000)
X = T*np.cos(T)
Y = T*np.sin(T)
plt.subplot(2,3,4)
plt.plot(X,Y)

T = np.linspace(0,2*np.pi,1000)
X = a*np.cos(T)
Y = b*np.sin(T)
plt.subplot(2,3,5)
plt.plot(X,Y)

T = np.linspace(0,2*np.pi,1000)
X = a*np.cos(T)
Y = b*np.sin(T)
plt.subplot(2,3,6)
plt.plot(X,Y)

T = np.linspace(0,100*np.pi,120)
X = a*np.cos(T)
Y = b*np.sin(T)
plt.subplot(2,3,6)
plt.plot(X,Y)

plt.show()


