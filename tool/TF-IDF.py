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
from math import sqrt
from array import array
from scipy.spatial.distance import euclidean

docs = pd.read_csv("file-name.csv")
docs = docs["2"]
spec_chars = ["!",'"',"#","%","&","'","(",")",
              "*","+",",","-",".","/",":",";","<",
              "=",">","?","@","[","\\","]","^","_",
              "`","{","|","}","~","–"]

for char in spec_chars:
    docs = docs.str.replace(char, ' ')
## 1 letter words seem to not count as words

vectorizer = TfidfVectorizer()

tf_idf = vectorizer.fit_transform(docs)

tf_idf = tf_idf.T.toarray()

df = pd.DataFrame(tf_idf, index=vectorizer.get_feature_names())

rows = len(df.columns)


def get_similar_tweets(q, df) :
    print("query:", q)
    
    
    q = [q]
    q_vector = vectorizer.transform(q).toarray().reshape(df.shape[0],)
    sim = {}
    
    
    print("Cosin similarity:")
    
    for i in range(rows):
        sim[i] = np.dot(df.loc[:,i].values, q_vector)/np.linalg.norm(df.loc[:, i])*np.linalg.norm(q_vector)
        
        sim_sorted = sorted(sim.items(), key = lambda x: x[1], reverse = False)
        

    
    for k, v in sim_sorted:         
        if v != 0.0 and v!= None :
            print("Similarity Values: ", v)
            print(docs[k])
            print()

        
            
        
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


