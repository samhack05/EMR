# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 18:07:10 2019

@author: ayush saxena
"""
#from sklearn.externals\
import joblib

Dclf = joblib.load('diabetes_classifierD.pkl')
Rclf = joblib.load('diabetes_classifierR.pkl')
Sclf = joblib.load('diabetes_classifierS.pkl')
def predict_diabetes(record):
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
        return("YOU MAY HAVE DIABETES")
    else:
        return("YOU'R SAFE! NO DIABETES")



