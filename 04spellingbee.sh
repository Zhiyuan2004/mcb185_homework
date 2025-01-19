cd ~/Code/MCB185/data/
gunzip -c dictionary.gz | grep "r" | grep -v "[^zonciar]" | grep "...."
gunzip -c dictionary.gz | grep "r" | grep -v "[^zonciar]" | grep "...." | wc -l 

Now try a new example: middle words: p ; other 6 words: AYETHL
gunzip -c dictionary.gz | grep "p" | grep -v "[^ayethlp]" | grep "...."
gunzip -c dictionary.gz | grep "p" | grep -v "[^ayethlp]" | grep "...." | wc -l

