# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 18:58:07 2019

@author: ayush saxena
"""

#from sklearn.externals\
import joblib

Dclf = joblib.load('indian_liver_classifierD.pkl')
Rclf = joblib.load('indian_liver_classifierR.pkl')
Sclf = joblib.load('indian_liver_classifierS.pkl')

def liver_Predict(record):
    record2=[]
    record2.append(record)
    R=Rclf.predict(record2)    
    D=Dclf.predict(record2)    
    S=Sclf.predict(record2)    
    final=0

    if(R==S or R==D):
        final=R
    elif(S==D):
        final=S
        
    if(final==1):
        return("YOU MAY HAVE LIVER PROBLEMS")

    return("YOU'R SAFE! NO LIVER PROBLEMS")

