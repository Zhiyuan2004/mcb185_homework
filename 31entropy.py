import sys
import math

probs = [] # create new list
for arg in sys.argv[1:]: # loops through all command-line arguments, use a slice to skip the first argument(name of program)
	f = float(arg) # convert argument to float number
	if f <= 0 or f >= 1: sys.exit('error: not a probability') # the probability should be in range of 0-1
	probs.append(float(arg)) # adds the probability in provs list
	
total = 0
for p in probs: total += p
if not math.isclose(total,1.0):
	sys.exit('error: probs must sum to 1.0')

h = 0
for p in probs:
	h -= p * math.log2(p) # equivalent h = h− (p * math.log2(p))

print(f'{h:.4f}')
