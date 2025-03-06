import gzip
import sys

with gzip.open(sys.argv[1], 'rt') as fp: # open a gzip-compressed file
    for line in fp: # iterate each line in the file
        if line[0] != '#': #skip comment line, when you open the file, there is some comment line
            words = line.split() # splits the line into a list of words based on whitespace
            if words[2] == 'CDS': # third column, find CDS
                beg = int(words[3]) # forth column, begin
                end = int(words[4]) # fifth column, end 
                print(end - beg + 1) # the length of CDS

with gzip.open(sys.argv[1], 'rt') as fp:
    for line in fp:
        if line[0] == '#': continue 
        # continue is used to use immediately end the current iteration of the loop
        words = line.split()
        if words[2] != 'CDS': continue
        beg = int(words[3])
        end = int(words[4])
        print(end - beg + 1)


# != means not equal to