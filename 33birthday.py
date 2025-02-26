import random
import sys

# Read command-line arguments
trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

shared = 0

for i in range(trials):
	birthday = [] # create empty list to store birthdays
	
	for i in range(people):     # Generate birthdays using list.append()
		bday = random.randint(0,days-1)
		birthday.append(bday)

	has_duplicate = False  # Check for shared birthdays using nested loops
	for i in range(len(birthday)):
		for j in range(i + 1, len(birthday)):
			if birthday[i] == birthday[j]:
				has_duplicate = True
				break
		if has_duplicate:
			break
			
	if has_duplicate:
		shared += 1

prob = shared / trials
print(f'{prob:.2f}')