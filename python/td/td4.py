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
def syracuse(a,n) :
	if a != int(a) and a < 0 :
		a = input('Give me the "a" value : ')
	if n != int(n) and n < 0 :
		n = input('Give me the "n" value : ')
	x = a
	for i in range(n+1) :
		if (x % 2) == 0 :
			x = x/2
		elif x == 1 :
			x = 1
		else :
			x = 3 * x + 1
		n += 1
	result = x
	return result
#print(syracuse(2, 5))
# Exercice 2
# (1)
def recherche1(chaine, mot) :
	for i in range(len(chaine)) :
		if chaine[i:len(mot)+i] == mot :
			return True
	return False	
# (2)
def recherche2(chaine, mot) :
	if mot in chaine :
		return True
	else :
		return False
# (3)
def compte(chaine, mot) :
	return chaine.count(mot)
#print(recherche2('aaaaa', 'aa'), ' ', compte('aaaaa', 'aa'))
# Exercice 3
# (1)
	# (a)
def palindrome1(mot) :
	if mot == mot[::-1] :
		return True
	else :
		return False
#print(palindrome1('boab'))
	#(b)
def palindrome2(mot) :
	i = 0
	k = len(mot)-1
	while i < k :
		while mot[i] == ' ':
			i += 1
		while mot[k] == ' ':
			k -= 1
		if mot[i] != mot[k] :
			return False
		i += 1
		k -= 1
	return True
#print(palindrome2('boba'))
# (2)
	# (a)
def delspace(ph) :
	l = list(ph)
	for i in range(len(l)) :
		if ' ' in l :
			l.pop(l.index(' '))
	return str(l)
#print(delspace('bobbob'))
	# (b)
def Palindrome(mot) :
	return palindrome2(mot)
print(Palindrome('bob bob'))
# Exercice 4

# Exercice 5

