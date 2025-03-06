# create a library for sequence
def transcribe(dna):
	return dna.replace('T', 'U')

def revcomp(dna):
	rc = [] # create a list rc to hold new sequence
	for nt in dna[::-1]:
		if 	 nt == 'A': rc.append('T')
		elif nt == 'C': rc.append('G')
		elif nt == 'G': rc.append('C')
		elif nt == 'T': rc.append('A')
		else: 			rc.append('N')
	return ''.join(rc)
	
