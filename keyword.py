# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 20:07:32 2021

@author: moeez
"""

from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
text= open("subtitle.txt", "r")
   
    #print(text.read())
data = text.read()
   # print(data)
wordToken = word_tokenize(data)
print(wordToken)
t= 1
#Tokenizer
tokenizer = RegexpTokenizer(r'\w+')
tok = tokenizer.tokenize(data)
print(tok)

#remove stop word
stop_word = set(stopwords.words("english"))
sw = []
for word in tok:
    if word not in stop_word:
print(sw)



text.close()