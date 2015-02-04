'''a = 0
k = 1
while a < 5 :
	a = a + (1/k)
	k += 1
print(str(k))'''

def arithmetico_geom(a,q,r,N) :
	i = 1
	result = a
	while i < N :
		result = q * result + r
		i += 1
	return result
#print(arithmetico_geom(1,3,-1,10))

def syracuse(n) :
	i = 0
	a = 7
	result = [a]
	while i < n :
		if a % 2 == 0 :
			a = a/2
		else :
			a = 3*a+1
		result.append(a)
		i += 1
	return result
#print(syracuse(100))

'''a = list(range(1,101))
b = list(range(1,101))
c = list(range(1,101))
borgne = [ a for a in range(101) and b for b in range(101) and c for c in range(101) for a**2 + b**2 == c**2 ]
print(borgne)'''
