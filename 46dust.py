import sys
import math
import mcb185

def calculate_entropy(sequence):
	nts = 'ACGT'
	counts = [0] * len(nts) # Initialize counts for A, C, G, T
	# count occurrences of each nucleotide
	for nt in sequence:
		idx = nts.find(nt)
		if idx != -1: # ignore non-ACGT characters
			counts[idx] += 1
	
	total = sum(counts)
	if total == 0:
		return 0 # If sequence is empty or has no valid nucleotides
	
	entropy = 0 
	for count in counts:
		if count > 0:
			p = count / total
			entropy -= p * math.log2(p)
	return entropy

def mask_low_complexity(sequence, window_size, entropy_threshold):
	masked_sequence = list(sequence)  # convert sequence into list
	for i in range(len(sequence) - window_size + 1):
		window = sequence[i:i + window_size]
		entropy = calculate_entropy(window)
		if entropy < entropy_threshold: # compare with entropy threshold
			for j in range(i, i + window_size):
				masked_sequence[j] = 'N' # change all low-complexity regions to 'N'
	return ''.join(masked_sequence)

def wrap_sequence(sequence, line_length=60):
    return '\n'.join(sequence[i:i + line_length] 
    for i in range(0, len(sequence), line_length))

fasta_file = sys.argv[1]
window_size = int(sys.argv[2])
entropy_threshold = float(sys.argv[3])
line_length = 60

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	new_seq = mask_low_complexity(seq, window_size, entropy_threshold)
	wrapped_seq = wrap_sequence(new_seq)

print(wrapped_seq)