'''
 * Copyright 2014  Bastien PEDERENCINO <zeromus.linux@gmail.com>
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WHITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more detail.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor,
 * Boston, MA  02110-1301  USA
'''
# All imports
import math
from math import log
import fractions
from time import clock
from random import random
# Exercice 1
	# (1)
		# (a)
def suite1(n) :
	result = [ ]
	for i in range(n) :
		result.append(12 * i + 1)
	return result
#print(suite1(3))
		# (b)
def suite2(n) :
	return [12*i+1 for i in range(n)]
	# (2)
def duree(fonction, n = 1000000) :
	start = clock()
	fonction(n)
	end = clock()
	return str(end - start)
#print("Temps d'execution :\n Methode 1 : " + duree(suite1) + "\n Methode 2 : " + duree(suite2))

# Exercice 2
	# (1)
def moyenne(liste) :
	if (liste != []) :
		return sum(liste) / len(liste)
#L = [ random() for i in range(100) ]
#moyenne(L)
	# (2)
def variance(liste) :
	if (liste != []) :
		Esp = moyenne(liste)
		liste2 = [(x-Esp)**2 for x in liste]
	# (3) 

# Exercice 3
	# (1)
#print([log(x) for x in range(1,20)])
	# (2)
print([[x for x in range(100)] for ])

