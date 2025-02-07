import math

limit = 100
for a in range(1,limit): #try from smaller number
	for b in range(a+1,limit):  # b loop in a loop 
		c = math.sqrt(a ** 2 + b ** 2)
		remainder = c % 1  # one way to get integer
		if remainder == 0: print(a,b,c)
		