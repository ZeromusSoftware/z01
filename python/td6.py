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
# 1)
#	a)
def recherche1(l,e) :
	return (e in l)
#	b)
def recherche2(l,e) :
	for x in l :
		if x == e :
			return True
	return False
# 2)
#	a)
def dich_search1(l,e) :
	while len(l) > 1 :
		i = len(l) // 2
		if e == l[i] :
			return True
		elif e < l[i] :
			l = l[:i]
		else :
			l = l[i:]
	if(len(l) == 1 and l[0] == e) :
		return True
	return False		
#	b)
def dich_search2(l,e) :
	Imin, Imax = 0, len(l)-1
	while Imax - Imin >= 0 :
		Imed = (Imin + Imax) // 2
		if e == Imed :
			return True
		elif e < Imed :
			Imin = Imed + 1
		else :
			Imax =Imed - 1
	return False
# 3)
def ttime(seekf) :
	from random import random
	L = [random() for k in range(100000)]
	L.sort()
	from time import clock
	a = clock()
	seekf(L, 0)
	b = clock()
	print(b-a, 'secondes pour ' + str(seekf))
'''
# Test final
ttime(recherche1)
ttime(recherche2)
ttime(dich_search1)
ttime(dich_search2)
'''
# Exercice 2
f = lambda x : x**3-3*x**2+1
def rpz(f) :
	import numpy as np
	import matplotlib.pyplot as plt
	x = np.linspace(0,2,1000)
	y = f(x)
	plt.figure('exercice 2')
	plt. plot(x,y)
	plt.grid()
# 1)
#print(f(0))
#print(f(2))
# 2)
def dich_solve(f, a, b, e) :
	assert f(a) * f(b) <= 0
	while e < abs(b - a) :
		m = (a + b) /2
		if f(a) * f(m) < 0 :
			a,b = a,m
		else :
			a,b = m,b
		return (a + b) /2
print(dich_solve(f, 0, 2, 0.001))
# 3)
