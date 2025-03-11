import sys
import mcb185

kdscale = {
	'I':  4.5, 'V':  4.2, 'L':  3.8, 'F':  2.8, 'C':  2.5,
	'M':  1.9, 'A':  1.8, 'G': -0.4, 'T': -0.7, 'S': -0.8,
	'W': -0.9, 'Y': -1.3, 'P': -1.6, 'H': -3.2, 'E': -3.5,
	'Q': -3.5, 'D': -3.5, 'K': -3.9, 'N': -3.5, 'R': -4.5,
}

def cal_kd(seq):
	kd = 0
	for aa in seq:
		kd += kdscale[aa]
	return kd / len(seq)

def peptide(protein,w,t): 
	for i in range(len(protein) - w + 1):
		window = protein[i:i+w]
		if 'P' in window:
			continue #skip windows containing proline 
		kd = cal_kd(window)
		if kd >= t:
			return True
		return False

fasta_file = sys.argv[1] 
#~/Code/MCB185/data/GCF_000005845.2_ASM584v2_protein.faa.gz
for defline, protein in mcb185.read_fasta(fasta_file):
	if peptide(protein[:30],8,2.5) and peptide(protein[30:],11,2):
		print(defline)