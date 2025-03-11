import sys
import math

colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])


# function to calculate distance
# taxi-cab distance
def dtc(P, Q):
	d = 0
	for p, q in zip(P, Q):
		d += abs(p - q)
	return d

# square root distance
def dtc(P,Q): 
	d = 0
	for p, q in zip(P,Q):
		d += (p - q)**2
	return math.sqrt(d)

fp = open(colorfile)
mindis = 255*3 # maximum possible distance

for line in fp:
 	words = line.split() #split based on space
 	colorname = words[0]
 	r,g,b = words[2].split(',')
 	rgb = int(r), int(g),int(b)
 	dis = dtc((R,G,B),rgb)
 	if mindis > dis:
 		mindis = dis # update mindis
 		mincolorname = colorname
print(mincolorname)

fp.close()