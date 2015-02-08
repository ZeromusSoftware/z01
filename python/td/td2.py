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
def abs(int) :
	if int < 0 : 
		int = -int
	result = int
	return result
#print(abs(-4))	

# Exerice 2
def fact(int) :
	int = abs(int)
	i = 1
	j = 1
	while i <= abs(int) :
		j = j * i
		i = i + 1
	result = j
	return result
#print(fact(-4))

# Exercice 3
def E(float) :
	if float < 0 :
		x = float - int(float)
		float  = float - 1
		if x == 0 :
			float +=  1
	float = int(float)
	result = float
	return result
#print(E(-3))

# Exercice 4
def exa(int) :
	i = 0
	result = ''
	while int > 0 :
		i += 1
		x = int % 16
		if x == 10 :
			x = 'A'
		if x == 11 :
			x = 'B'
		if x == 12 :
			x = 'C'
		if x == 13 :
			x = 'D'
		if x == 14 :
			x = 'E'
		if x == 15 :
			x = 'F'
		result = str(x) + ' ' + result
		int = int // 16
	result = result
	return result
#print(exa(28))

# Exercice 5
def pgcd(a,b) :
	while True :
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
		if reste == 0 : 			
			return str(b)
		a , b = quotient , reste 
#print(pgcd(4,8))

# Exercice 6
def ppcm(x,y) :
	if y > x :
		x , y = y , x
	i = 2
	while True :
		if x % y == 0 :
			return str(x)
		x = x * i
		i += 1
def menu() :
	ligne1 = "1 - Calculer le PGCD de deux entiers \n"
	ligne2 = "2 - Calculer le PPCM de deux entiers \n"
	ligne3 = "3 - Déterminer si un nombre est premier \n"
	ligne4 = "4 - Donner la décomposition en facteurs premiers d'un nombre \n"
	ligneq = "q - Quitter \n"
	ligneu = "\nVotre choix : "
	text = '\nMENU : \n' + ligne1 + ligne2 + ligne3 + ligne4 + ligneq + ligneu
	var = input(text)
	if var == '1' or var == '2' :
		x = input('Premier entier : ')
		y = input('Second entier : ')
	if var == '3' or var == '4' :
		x = input('Votre nombre : ')
	if var == '1' :
		print('Le PGCD de ' + x + ' et de ' + y + ' est ' + pgcd(int(x),int(y)))
	if var == '2' :
		print('Le PPCM de ' + x + ' et de ' + y + ' est ' + ppcm(int(x),int(y)))
	if var == '3' :
		print('borgne'+var)
	if var == '4' :
		print('borgne'+var)
	if var == 'q' :
		print('Bye bro ;)')
		return
	input()
	menu()
menu()
