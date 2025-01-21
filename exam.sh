cd ~/Code/MCB185/data/
gunzip -c A.thaliana.gff.gz | cut -f 3,7 | grep gene | sort | uniq -c
