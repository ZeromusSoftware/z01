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
import fractions

# Euclide-like algorithm
def euclide(int) : # decimal vers binaire
	mem = int
	result = str()
	i = 0
	while int > 0 :
		result =  str(int % 2) + result # reste
		int = int // 2 # quotien
		i += 1
	result = 'L\'ecriture binaire de ' + str(mem) + ' est : ' + result # affichage du resultat
	return result
#print(euclide(107)) 

def division(a,b) :
	quotient = int 
	reste = int
	if b > a :
		a,b = b,a
	condition = 0
	test = 0
	while test < a :
		test = b * condition
		condition += 1
	quotient = condition - 1
	while quotient * b > a :
		quotient -= 1 
	reste = a - (quotient * b)			
	result = str(a) + ' = ' + str(b) + ' * ' + str(quotient) + ' + ' + str(reste)	 
	return result
#print(division(4,7))


