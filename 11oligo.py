def tm(A,T,G,C): 
	total_nt = A + T + G + C
	if total_nt <= 13:
		return (A + T) * 2 + (G + C) * 4 
	elif total_nt > 13:
		return 64.9 + 41 * ( G + C - 16.4) / (A + T + G + C)
		
print(tm(5,7,3,4))
print(tm(2,2,3,3))
print(tm(10,10,15,15))

