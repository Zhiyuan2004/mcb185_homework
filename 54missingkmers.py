import sys
import mcb185
import itertools
import sequence

def missing_kmer(seq,k):
	kcount = {} # Use a dictionary to store observed k-mers
	# Check original sequence
	for i in range(len(seq) - k + 1):
		kmer = seq[i:i+k]
		kcount[kmer] = 1 # store k-mer as a key
	# check the reverse complement
	rc_seq = sequence.revcomp(seq)
	for i in range(len(rc_seq) - k + 1):
		kmer = rc_seq[i:i+k]
		kcount[kmer] = 1
	if len(kcount) < 4 ** k:
		return True
	return False

ecoligenome = sys.argv[1]
for defline, seq in mcb185.read_fasta(ecoligenome):
	k = 1 # Start with k=1
	while True:
		if missing_kmer(seq,k): # Check if there are missing k-mers for the current k
			print(f'k={k}:missing k-mers found')
			break  # Stop after finding the smallest k with missing k-mers
		k += 1 # Increment k and repeat the process
