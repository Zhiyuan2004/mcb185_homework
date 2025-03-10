import sys

colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])

# function to calculate distance
def dtc(P, Q):
	d = 0
	for p, q in zip(P, Q):
		d += abs(int(p) - int(q))
	return d

fp = open(colorfile)
mindis = 255*3 # maximum possible distance

for line in fp:
 	words = line.split() #split based on space
 	colorname = words[0]
 	colorNum = words[2].split(',')
 	rgb = [R,G,B]
 	dis = dtc(colorNum,rgb)
 	if mindis > dis:
 		mindis = dis # update mindis
 		mincolorname = colorname # find color name
print(mincolorname)

fp.close()