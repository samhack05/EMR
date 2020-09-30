# -*- coding: utf-8 -*-

"""
Created on Sun Sep 15 22:03:52 2019

@author: ayush saxena
"""

import pickle
#from sklearn.externals\
import joblib

#Dclf = joblib.load('disease_classifierD.pkl')
#Rclf = joblib.load('disease_classifierR.pkl')
Sclf = joblib.load('disease_classifierS.pkl')

filename ='disease_dictionary'
infile = open(filename,'rb')
disease_dictionary=pickle.load(infile)
infile.close() 

filename ='sym_dictionary'
infile = open(filename,'rb')
sym_dictionary=pickle.load(infile)
infile.close()
 
print("enter symtoms to predict diseases !! ENTER <E> to exit")
def pridict_sym(arr):
    record = [0] * 404
    for i in range(len(arr)):
        v = sym_dictionary[arr[i]]
        record[v]=1
        
    record2=[]
    record2.append(record)

    #a=Rclf.predict(record2)    
    #print(disease_dictionary[int(a)])
    #a=Dclf.predict(record2)    
    #print(disease_dictionary[int(a)])
    a=Sclf.predict(record2)    
    return(disease_dictionary[int(a)])


