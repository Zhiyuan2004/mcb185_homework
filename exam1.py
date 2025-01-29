import math

def dist(x1,y1,x2,y2):
	return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(dist(1,2,3,4))

def is_valid(num):
	if 0 <= num <= 1: return True
	return False
print(is_valid(0.5))
print(is_valid(2))

def harmonicmean(a,b,c,d):
	sum=(1/a)+(1/b)+(1/c)+(1/d)
	return sum/4
print(harmonicmean(1,2,3,4))



