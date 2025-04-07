# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 01:25:03 2019

@author: Asus
"""

import numpy as np
import math

## identifing query
#query=['data','mining','text']
query=['unstructured','mining','text']

#document
d1='data mining is a rather new field of study for discovering knowledge from data.this data can be numeric data or even a text,so data mining is of paramount importance.'
d2='text mining system makes an exchange of words from unstructured data into numerical values.'
d3='text mining also referred to as text data mining,roughly equivalent to text analytics,is the process of deriving high-quality information from text.'
## split of each word in each documend
w1=(d1.split())
w2=(d2.split())
w3=(d3.split())
## list of total word in each document
w=w1+w2+w3
  
index=list();
h=list()   # list for seprating dot
k=list()   # list for seprating comma
## gathering and seprating word with'.',','into two group
for i in range(0,len(w)):
  for x in range(0,len(w[i])):
    if w[i][x]==',':
     k.append( w[i].split(","))
     index.append(i);
    elif w[i][x]==".":
     h.append(w[i].split("."))
     index.append(i)
## list of word with '.',','   
Re=list()         
for j in range (0,len(index)):
    Re.append(w[index[j]])
    
 #change to list to set and set to list and seprating original vocabulary from word with dot and comma
Re_set=set(Re)
wset=set(w)
vocabulary=wset-Re_set
vocabulary=list(vocabulary)
#adding seprated word with dot and comma to original vocabulary
for i in  range (0,len(k)):
    for j in range (0,len(k[i])):
        vocabulary.append(k[i][j])
for i in  range (0,len(h)):
    for j in range (0,len(h[i])):
        if h[i][j]!='':
          vocabulary.append(h[i][j])
## remove duplicate word from vocabulary
word_duplicate=list()
word_alone=list()
for i in range (0,len(vocabulary)):
       if vocabulary.count(vocabulary[i])!=1:
           if vocabulary[i]  not in word_duplicate:
                 word_duplicate.append(vocabulary[i])
       elif  vocabulary.count(vocabulary[i])==1:
            word_alone.append(vocabulary[i])
vocabulary_final=word_duplicate+word_alone        
# word in each document
# word of each document in each list
docs=list()
docs.append(d1.split())
docs.append(d2.split())
docs.append(d3.split())
camma= [[],[],[]]
index_com=[[],[],[]]
dot=[[],[],[]]
## extract word wit dot and comma in each document
for n in range (len(docs)):
 for i in range(0,len(docs[n])):
  for x in range(0,len(docs[n][i])):
    if docs[n][i][x]==',': 
      camma[n].append( docs[n][i].split(","))
      index_com[n].append(i);
    elif docs[n][i][x]==".":
     dot[n].append(docs[n][i].split("."))
     index_com[n].append(i)
#remove word with dot and comma in each document            
res=[[],[],[]]    
for i in range(len(index_com)) :
    for j in range(len(index_com[i])):
        res[i].append(docs[i][index_com[i][j]])        
for i in range(len(docs)):
    doc_set=set(docs[i])
    res_set=set(res[i])
    doc_set=doc_set-res_set
    docs[i]=list(doc_set)
## adding separated word with camma and dot to word document    
for n in range (len(docs)):   
  for i in  range (0,len(camma[n])):
    for j in range (0,len(camma[n][i])):
        docs[n].append(camma[n][i][j])
for n in range (len(docs)):   
  for i in  range (0,len(dot[n])):
    for j in range (0,len(dot[n][i])):
     if dot[n][i][j]!='':
        docs[n].append(dot[n][i][j])
     
#Algoritm
#count(vocabulary,quary)
c_v_q=np.zeros((len(query),1))       
intersect_vocab_docs=[[],[],[]]         
vocabulary_final_set=set(vocabulary_final)
query_set=set(query)
intersect_query_vocab=query_set.intersection(vocabulary_final_set)
list_query_vocab=list(intersect_query_vocab)
for i in range(len(query)):
    if query[i] in list_query_vocab:
        c_v_q[i]=1
for j in range(len(docs)):
     for n in range(len(docs[j])):
          if docs[j][n] in vocabulary_final:
              intersect_vocab_docs[j].append(docs[j][n])
# count(vocablary,word document)
count=np.zeros((len(docs),len(query)))
total=np.zeros((len(docs),1))           
for n in range(len(intersect_vocab_docs)):
   for i in range (len(intersect_vocab_docs[n])):
        for j in range(len(query)):
         if  intersect_vocab_docs[n][i] in  query[j]:
             count[n][j]=count[n][j]+1
#adjusted TF-IDF and calculating f(q,d)
log_adjusted=list()  
doc_freq=np.zeros((len(docs),len(query)))
sum_freq=[0,0,0]
for  i in range(len(count)):
    for j in range(len(count[i])):
        if count[i][j]!=0:
            doc_freq[i][j]=1   
for i in range (len(doc_freq)) :
   for j in range (len(doc_freq[i])):  
    doc_freq_reverse=np.transpose(doc_freq)     
    sum_freq[i]=np.sum((doc_freq_reverse[i][:]))           
for n in range(len(count)) :
     for i in range(len(count[n])):
         total[n]=math.log10(len(docs)+1/sum_freq[i])*c_v_q[i]*count[n][i]+total[n]
 #choosing related document         
for i in range (len(docs)) :
    if total[i] == np.max(total)  :
        print('document=',i+1)
         
          
          
              
              
              
          
                
        
        
   
    
        

   
        
   
           


    

    
            
     
         
          


       
       
       
     
  
     
     
        



