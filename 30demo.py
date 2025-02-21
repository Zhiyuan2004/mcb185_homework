import math
import sys
print(sys.argv)

s = 'hello world'
print(s)
print(s.upper())
print(s.replace('o','').replace('r','i'))

print(f'{math.pi}')            # does nothing special
print(f'{math.pi:.3f}')        # 3 fixed digits after decimal
print(f'{1e6 * math.pi:e}')    # exponent notation (3.141593e+06)
print(f'{"hello world":>20}')  # right justify with space filler
print(f'{"hello world":.>20}') # right justify with dot filler
print(f'{20:<10} {10}')        # left justify
print('{} {:.3f}'.format('str.format', math.pi))  # str.format 3.142
print('%s %.3f' % ('printf', math.pi))

seq = 'GAATTC'
print(seq[0],seq[1]) # seq[0] is the first letter of the sequence
print(seq[-1]) # count backwards from the right
for nt in seq:
	print(nt, end='') # end= make it write in line
print()
for i in range(len(seq)):
	print(i, seq[i])

s = 'ABCDEFGHIJ'
print(s[0:5])  # 0 initial position; 5 end-before limit
print(s[0:8:2]) # ACEG
print(s[0:5], s[:5])        # both ABCDE
print(s[5:len(s)], s[5:])   # both FGHIJ
print(s, s[::], s[::1], s[::-1]) #why?

dna = 'ATGCTGTAA'
for i in range(0, len(dna), 3):
    codon = dna[i:i+3]
    print(i, codon)

tax = ('Homo','sapiens', 9606) # construct tuple
print(tax) # note the parentheses in the output
print(tax[0]) # index
print(tax[::-1]) # slice; :: omit start and stop, which means the slice will include the entire sequence.

nts = 'ACGT'
for i in range(len(nts)):
	print(i, nts[i])
for i, nt in enumerate(nts): # an alternative way 
	print(i,nt)
	
names = ('adenine','cytosine','guanine','thymine')
for i in range(len(names)):
	print(nts[i],names)
for nt, name in zip(nts,names):
	print(nt,name)
for i, (nt,name) in enumerate(zip(nts,names)):
	print(i,nt,name)

'''lists'''	
nts = ['A','T','C']
print(nts) # A T C
nts[2] = 'G'
print(nts) # A T G, list content are mutable
nts.append('C')	# add elements at the end of list
print(nts)
last = nts.pop() # remove elements from the end of list
print(last)
print(nts)
nts.sort() # sort by alphabetic
print(nts) # A G T
nts.sort(reverse=True)
print(nts)
nucleotides = nts
nucleotides.append('C')
print(nts, nucleotides) # change together, need "list.copy()"

item = list() # create empty lists
print(item)
item.append('eggs')
print(item)
stuff = []
stuff.append(3) # add integer 3 to the list
print(stuff)
alph = 'ACDEFGHIKLMPQRSVW'
print(alph)
aas = list(alph)
print(aas)
	
text = 'good day      to you'
words =text.split() # split each word
print(words)
line = '1.41,2.72,3.14'
print(line.split(','))

s = '-'.join(aas)
print(s)
s = ''.join(aas)
print(s)




