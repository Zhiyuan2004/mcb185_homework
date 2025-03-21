import sys
import sequence
import mcb185

def find_orfs(protein, frame, strand, offset):
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
        # Extract the ORF
		orfs.append((start, stop, frame, strand, protein[start:stop+1], offset)) # add ORF to the list
		start = stop + 1
	return orfs

# calculate genetics coordinates of ORF
def get_gff_coordinates(start, stop, frame, strand, offset):
    if strand == '+':
        gff_start = offset + frame + start * 3 + 1
        gff_end = offset + frame + stop * 3 + 3
    else: # reverse strand
        gff_start = offset + len(seq) - (frame + stop * 3 + 3)
        gff_end = offset + len(seq) - (frame + start * 3 + 1)
    return gff_start, gff_end

fasta_file = sys.argv[1]
min_length = int(sys.argv[2])

for defline, seq in mcb185.read_fasta(fasta_file):
    orfs = []
    for frame in range(3):
        # Forward strand
        protein = mcb185.translate(seq[frame:]) # translate protein
        orfs.extend(find_orfs(protein, frame, '+', frame)) # Find ORFs and add them to the list
        # Reverse strand
        rc_seq = sequence.revcomp(seq)
        protein = mcb185.translate(rc_seq[frame:])
        orfs.extend(find_orfs(protein, frame, '-', frame))
    # Filter ORFs by minimum length
    orfs = [orf for orf in orfs if len(orf[4]) >= min_length]
    # print our ORF feature
    for i, (start, stop, frame, strand, protein, offset) in enumerate(orfs):
        seq_id = defline.split()[0]
        prot_id = f"{seq_id}-prot-{i}"
        gff_start, gff_end = get_gff_coordinates(start, stop, frame, strand, offset)
        print(f"{seq_id}\tCDS\t{gff_start}\t{gff_end}\t{strand}\t0\tID={prot_id}")