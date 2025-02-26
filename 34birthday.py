import random 

shared = 0
trials = 100
days = 365
students = 23

for t in range(trials):
	calendar = []
	for i in range(days):
		calendar.append(0)
	
	for i in range(students):
		bday = random.randint(0, days-1)
		calendar[bday] += 1
		
	is_shared = False
	for day in range(len(calendar)):
		if calendar[day] > 1:
			is_shared = True
			break
	if is_shared:
		shared += 1
	print(f'trial{t+1}: {calendar}')
