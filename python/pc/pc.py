import math as m
import numpy as np # probleme de librairie
import matplotlib.pyplot as plt # probleme de librairie

t = np.linspace(0, 4*m.pi, 100)
# y = [m.cosx for x in t]

plt.plot(t, m.cos(t), color = 'b') # creation de la courbe du cosinus
plt.show() # affichage de la courbe
