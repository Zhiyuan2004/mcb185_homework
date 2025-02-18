import random

ins = 0
tot = 0

while True:
	x = random.random()
	y = random.random()

	if x ** 2 + y ** 2 < 1:
		ins += 1
	tot += 1
	pi = (ins/tot) * 4
	print(pi)
	
