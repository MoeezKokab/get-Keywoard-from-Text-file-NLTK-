# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 20:07:32 2021

@author: moeez
"""

from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
#read text from text file
text= open("subtitle.txt", "r")

# covert into str
data = text.read()

#Tokenizer
tokenizer = RegexpTokenizer(r'\w+')
tok = tokenizer.tokenize(data)
#print(tok)

#remove stop word
stop_word = set(stopwords.words("english"))
sw = []
for word in tok:
    if word not in stop_word:
        sw.append(word)
#print(sw)

# stemmer
stemmer = []
from nltk.stem import PorterStemmer
ps = PorterStemmer()
for word in sw:
        stemmer.append(ps.stem(word))
print(stemmer)
        
#correect spell
from autocorrect import spell
cw =[]
for word in stemmer:
    cw.append(spell(word))

# frq
from collections import Counter
frq = Counter(cw)
#print(frq)
ls=[]
for key in frq.keys():
    ls.append(key)
ls.sort()
print(ls)
#save keywoard
text_file = open("keywoards.txt", "w")
text_file.write(str(ls))
text_file.close()

text.close()
