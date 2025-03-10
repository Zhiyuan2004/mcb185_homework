import sys
import sequence
import mcb185

def find_orfs(protein, frame, strand):
	# Extract proteins from a translated sequence
	orfs = []
	start = 0
	while start < len(protein):
		# Find the start codon 'M'
		start = protein.find('M', start)
		if start == -1:
			break
        # Find the stop codon '*'
		stop = protein.find('*', start)
		if stop == -1:
			break
        # Extract the orf
		orfs.append((start, stop, frame, strand, protein[start:stop+1]))
		start = stop + 1
	return orfs

def wrap_sequence(sequence, line_length=60):
    return '\n'.join(sequence[i:i + line_length] 
    for i in range(0, len(sequence), line_length))

# Process each sequence in the FASTA file
fasta_file = sys.argv[1]
min_length = int(sys.argv[2])

for defline, seq in mcb185.read_fasta(fasta_file):
    orfs =[]
    # Six-frame translation
    for frame in range(3):
        # Forward strand
        protein = mcb185.translate(seq[frame:])
        orfs.extend(find_orfs(protein, frame, '+'))
        # Reverse strand
        rc_seq = sequence.revcomp(seq)
        protein = mcb185.translate(rc_seq[frame:])
        orfs.extend(find_orfs(protein, frame, '-'))
    # Filter ORFs by minimum length
    orfs = [orf for orf in orfs if len(orf[4]) >= min_length]
    for i, (start, stop, frame, strand, protein) in enumerate(orfs):
        # Generate a unique identifier
        seq_id = defline.split()[0]  # Use the first part of the defline
        prot_id = f"{seq_id}-prot-{i}"
        # Print the protein in FASTA format
        print(f">{prot_id}")
        print(wrap_sequence(protein))

