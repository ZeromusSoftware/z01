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
# Exercice 1
#	(1)
from math import *
def racine_trinome(a,b,c) :
	assert a != 0 # vérification du terme de degre 2
	d = b**2 - 4*a*c # calcul du discriminant
	if d != 0 :
		x = (-b-(d**0.5))/(2*a)
		y = (-b+(d**0.5))/(2*a)
		return (x, y)
	else :
		x = (-b)/(2*a)
		return x
#	(2)
'''print(racine_trinome(1,1,(1.0-2**-54)/4.0))'''
#	(3)
'''e = -54
a, b, c = 1, 1, (1.0-2**e)/4.0
print(racine_trinome(a,b,c))'''
# Exercice 2
#	(1) : les racines; x_n tend vers une racine
#	(2)
def newton(f,df,x,n) :
	for i in range(n) :
		x = x - f(x) / float(df(x))
	return x
#	(3)
'''f = lambda x : x**3-3*x**2+1
df = lambda x : 3*x**2 - 6*x'''
'''f = lambda x : x**2 - 2
df = lambda x : 2*x
print(newton(f,df,1,5))'''
# Exercice 3
def heron(a,n) :
	x = a
	for i in range(n) :
		x = 0.5 * (x + a/x)
	return x
	
