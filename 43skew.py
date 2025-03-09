import sequence

seq = 'ACGTACGTGGGGGACGTACGTCCCCC'
w = 10 # the sequence will be analyzed in segments (windows) of 10 nucleotides each.
for i in range(len(seq) - w + 1):
	s = seq[i:i+w]
	print(i, sequence.gc_comp(s),sequence.gc_skew(s))