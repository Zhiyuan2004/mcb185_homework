import sys
import math

list = []
for arg in sys.argv[1:]:
	f = float(arg)
	list.append(f)

def minmax(vals):
	mini = vals[0]
	maxi = vals[0]
	for val in vals:
		if val < mini: mini = val
		if val > maxi: maxi = val
	return mini, maxi
	
def mean(vals):
	total = 0
	for val in vals: 
		total += val
	return total / len(vals)

def SD(vals):
	variance = 0
	for val in vals:
		variance += (val - mean(list)) **2
	return math.sqrt(variance/len(list))

def median(vals):
	n = len(vals)
	sorted_vals = sorted(vals) # Sort the list once
	if n % 2 == 1:
		return sorted_vals [n//2]
	else: 
		 return (sorted_vals[n // 2 - 1] + sorted_vals[n // 2]) / 2


print(list)
print(minmax(list))
print(mean(list))
print(SD(list))
print(median(list))
	

