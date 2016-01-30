import nltk
import os
t=nltk.word_tokenize(open("D:\DFE\Gravity (film).txt",'r').read())
a=nltk.pos_tag(t)


def categorizeation(text):
	b=open("D:\DFE\\tt.txt",'w')
	
	for c in text:
		if (c[1]=='NN') or (c[1]=='NNS') or (c[1]=='NNP') or (c[1]=='NNPS') or (c[1]=='VB') or (c[1]=='VBD') or (c[1]=='VBG') or (c[1]=='VBN') or (c[1]=='VBP') or (c[1]=='VBZ'):	
			b.writelines(str(c)) 
	
	
	
		


categorizeation(a)


