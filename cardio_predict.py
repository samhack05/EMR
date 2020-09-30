# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 21:08:15 2019

@author: ayush saxena
"""

#from sklearn.externals\
import joblib

Dclf = joblib.load('cardio_classifierD.pkl')
Rclf = joblib.load('cardio_classifierR.pkl')
Sclf = joblib.load('cardio_classifierS.pkl')

def predict(record):
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
        
    if(final):
        return("YOU MAY HAVE CARDIOVASCULAR DISEASE")
    else:
        return("YOU'R SAFE! NO CARDIOVASCULAR DISEASE")

