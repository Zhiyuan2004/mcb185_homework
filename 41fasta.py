import sys
import mcb185

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	print(defline[:30],seq[:40],len(seq))
	
# run like this: 
# python3 41fasta.py ../MCB185/data/A.thaliana.fa.gz
# python3 41fasta.py ../MCB185/data/C.elegans.fa.gz
# python3 41fasta.py ../MCB185/data/D.melanogaster.fa.gz