import math

def dist(x1,y1,x2,y2):
	return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(dist(1,2,3,4))

def is_valid(num):
	if 0 <= num <= 1: return True
	return False
print(is_valid(0.5))
print(is_valid(2))

def mean3(a,b,c,d): 
	sum = a+b+c+d
	return sum/4
print(mean3(1,2,3,4))


