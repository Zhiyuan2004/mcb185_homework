import math

print('hello again') # greeting
print(1.5e-2)
print(1+1)
print(1-1)
print(2*2)
print(1/2)
print(2**3) # exponentiation
print(5//2) # integer divide
print(5%2) # remainder
print(5*(2+1))
print(abs(-2))
print(pow(2,3)) # 2 to the power of 3
print(round(3.1415926, ndigits=3))
print(0.1 * 3)
print(math.pow(2,3))
print(math.log(2))

a = 3
b = 4
c = math.sqrt(a**2 +b**2)
print(c)
print(type(a),type(b),type(c))  # int, int, float
print(type(a),type(b),type(c), sep=',', end='!\n')

def pythagoras(a,b):
	return math.sqrt(a**2 + b**2)
print(pythagoras(3, 4))

def circle_area(r): return math.pi * r**2
print(circle_area(3))
	
def ftoc(f):
	return (f - 32)/9*5
print(ftoc(98.6))

def mtok(m):
 	return (m/0.62)
print(mtok(62))

def mean3(a,b,c): 
	sum = a+b+c
	return sum/3
print(mean3(1,2,3))

def harmonicmean(a,b,c):
	sum=(1/a)+(1/b)+(1/c)
	return sum/3
print(mean3(1,2,3))

def diffmean(a,b,c):
	harmonic = harmonicmean(a,b,c)
	mean = mean3(a,b,c)
	return abs(mean-harmonic)
print(diffmean(4,5,6))

def dist2(x1,y1,x2,y2):
	x_dist = x2 - x1
	y_dist = y2 - y1
	return math.sqrt(x_dist ** 2 + y_dist ** 2)
print (dist2(0,0,3,4))

s = 'hello world' #strings
print(s, type(s))

a = 2
b = 2
c = a == b
print(c)
print(type(c))

if a < b or a > b: print('all things being equal')
if a < b and a > b: print ('you')
if not False: print(True)

a = 0.3
b = 0.1 * 3
if a < b: print('a < b')  # NEVER test for equality with floating point numbers.
elif a > b: print('a > b')
else: print('a == b')
print(abs(a-b))
if abs(a-b) < 1e-9: print('close enough')
if math.isclose(a,b): print('close enough')

s1 = 'A'
s2 = 'B'
s3 = 'a'
if s1 < s2: print('A < B')
if s2 < s3: print('B < a')

def silly(m,x,b): y = m * x + b
print(silly(2,3,4)) # get "None" because of no return