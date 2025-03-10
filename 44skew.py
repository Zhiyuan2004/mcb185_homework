import sequence
import gzip
import sys
import mcb185

'''
# this way is slow way
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	w = 1000
	for i in range(len(seq) - w + 1):
		s = seq[i:i+w]
		print(i, sequence.gc_comp(s),sequence.gc_skew(s))'''

# this way is faster way
for defline, seq in mcb185.read_fasta(sys.argv[1]):
    w = int(sys.argv[2]) 
    # Initialize counts for the first window
    window = seq[:w]
    g = window.count('G')
    c = window.count('C')
    print(sequence.gc_comp(window),sequence.gc_skew(window))
   
    # Slide the window across the sequence
    for i in range(1, len(seq) - w + 1):
        # Nucleotide leaving the window
        left = seq[i-1]
        if left == 'G':
            g -= 1
        elif left == 'C':
            c -= 1

        # Nucleotide entering the window
        right = seq[i+w-1]
        if right == 'G':
            g += 1
        elif right == 'C':
            c += 1
        
        print(i,(g+c)/w, (g-c)/(g+c))
        
        # command line: time python3 44skew.py ~/Code/MCB185/data/GCF_000005845.2_ASM584v2_genomic.fna.gz 10000