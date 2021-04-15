# -*- coding: utf-8 -*-

"""
Created on Fri Apr  9 18:05:42 2021
Search Alg
@author: Thomas Devan
"""

from sklearn.feature_extraction.text import TfidfVectorizer
import re
import pandas as pd
import numpy as np

docs = "pizza" , "izz", "pizza 0", "pizza 0 izz", "horse", "cow", "cow dog"

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(docs)

X = X.T.toarray()

df = pd.DataFrame(X, index=vectorizer.get_feature_names())

def get_similar_tweets(q, df) :
    print("query:", q)
    print("Cosin similarity:")
    
    q = [q]
    q_vector = vectorizer.transform(q).toarray().reshape(df.shape[0],)
    sim = {}
    rows = len(df.columns)
    
    for i in range(rows):
        sim[i] = np.dot(df.loc[:,i].values, q_vector)/np.linalg.norm(df.loc[:, i])*np.linalg.norm(q_vector)
        
        sim_sorted = sorted(sim.items(), key=lambda x: x[1], reverse= True)
        

    
    for k, v in sim_sorted:
        if v != 0.0 and v!= None :
            print("Similarity Values: ", v)
            print(docs[k])
            print()
                
            
q1 = input("Enter your search: ")
get_similar_tweets(q1, df)

