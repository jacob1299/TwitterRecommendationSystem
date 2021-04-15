# -*- coding: utf-8 -*-

"""
Created on Fri Apr  9 18:05:42 2021
Search Alg
@author: Robot
"""

from sklearn.feature_extraction.text import TfidfVectorizer
import re
import pandas as pd
import numpy as np
from math import log
from array import array
from scipy.spatial.distance import euclidean

raw = pd.read_csv("file-name.csv")
users = raw["3"]
docs = raw["2"]
users = users.str.replace("b'", '')
users = users.str.replace("'", '')
spec_chars = ["\n","!","#",".","/",":",";","?","@","[","\\","]","^","_",
              "`","{","|","}","~","–",")","("]

for char in spec_chars:
    docs = docs.str.replace(char, ' ')
## 1 letter words seem to not count as words

vectorizer = TfidfVectorizer()

tf_idf = vectorizer.fit_transform(docs)

tf_idf = tf_idf.T.toarray()

df = pd.DataFrame(tf_idf, index=vectorizer.get_feature_names())

rows = len(df.columns)

sim = {}

N = 1

second = 0

top = 0

def get_similar_tweets(q, df) :
    print("query:", q)
    
    
    q = [q]
    q_vector = vectorizer.transform(q).toarray().reshape(df.shape[0],)
    sub = 0
        
    
    for i in range(rows):
        sim[i] = np.dot(df.loc[:,i].values, q_vector)/np.linalg.norm(df.loc[:, i])*np.linalg.norm(q_vector)

    sim_sorted = sorted(sim.items(), key = lambda x: x[1], reverse = False)
        

    
    for k, v in sim_sorted:         
        if v != 0.0 and v!= None :
            global N 
            N = N + 1
            global second
            second = sub
            global top
            top = k            
            print("Similarity Values: ", v)
            print("User :", users[k])
            print("Post ID: ", k)
            sub = k
            print(docs[k])
            print()
        
    print("-----------------\n")
            
        
#def euclidean(df):
#    m = 0
#    for j in df:
#        m = m+1
#        dist = array('l')
#        dist = dist.append(euclidean(df[m],df[m-1]))
#    print(dist)
#    return dist
#    print(dist)

q1 = input("Enter your search: ")
get_similar_tweets(q1, df)
##euclidean(df)



def avg_leng():
    avg = 0
    for p in range(rows) :
        avg = avg + len(docs[p])
    avg = avg / len(docs)
    return avg


bmval = {}


def bm25(q):
    
    avg = avg_leng()
    for i in range(rows):
        bmval[i] = ((log(rows/N))*((2.2*sim[i]*len(docs[i]))/((len(docs[i])+2.2)*(0.25+0.75*avg))))
        
    bmval_sorted = sorted(bmval.items(), key = lambda z: z[1], reverse = False)
        
    for d, t in bmval_sorted:         
        if t != 0.0 and t!= None :
            print("BM25 Values: ", t)
            print("User :", users[d])
            print("Post ID: ", d)
            print(docs[d])
            print()

bm25(q1)


def recommend(q):
    get_similar_tweets(docs[q], df)
        

def recommendtest():
    recommend(top)
    for i in range(2):
        get_similar_tweets(docs[second], df)
    
