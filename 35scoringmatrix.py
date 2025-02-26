import sys

alphabet = sys.argv[1]
match_score = sys.argv[2]
mismatch_score = sys.argv[3]

# step 2: Turn my scores into numbers
match_score = int(sys.argv[2])
mismatch_score = int(sys.argv[3])

# print first row in line
print('  ', end= ' ') # just add space before A
for letter in alphabet:
	print(letter, end='  ') # add space between letter in the first row
print()
# print everything in the nested loop: 
for letter1 in alphabet:
	print(letter1, end=' ')
	for letter2 in alphabet:
		if letter1  == letter2:
			print('+1', end=' ')
		else:
			print('-1', end=' ')
	print()
	