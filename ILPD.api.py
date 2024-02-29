# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 19:01:43 2023

@author: Lenovo
"""

import numpy as np
import pickle as pk
import streamlit as st
 

t=pk.load(open("C:\Users\Lenovo\Desktop\Hackathon1\ILPD_Logistic.sav","rb"))
t=pk.load(open("C:\Users\Lenovo\Desktop\Hackathon1\LogisticR_model.sav","rb"))
a=pk.load(open("C:\Users\Lenovo\Desktop\Hackathon1\trained_model.sav",'rb'))


def diabetic_predictive_system(t):
    y=np.asarray(t)
    u=y.reshape(1,-1)
    i=a.predict(u)
    print(i)
    if(i==1):
        a=""
        return a
    else:
      return "it is not diabatics"

def  stroke_predictive_system(t):
    k=np.asarray(t)
    j=k.reshape(1,-1)
    h=t.predict(j)
    print(h)
    if(h==0):
      return"the person is not suffering from stroke"
    else:
      return"the person is  suffering from stroke"
def Predictive_System(l):

    k=np.asarray(l)
    j=k.reshape(1,-1)
    h=t.predict(j)
    if(h==0):
        return ("Person is not suffer from liver problem")
    else:
        return ("Person is  suffer from liver problem")
def main():
    st.title("PERSONAL HEALTHCARE  SYSTEM")
    name=st.text_input("Give the prediction model you would like to choose: ")
    if name.lower()=="liver":
        st.title("LIVER INFECTION CHEAKUP SYSTEM")
        age=st.number_input("AGE")
        gender=st.number_input("gender:")
        tot_bilirubin=st.number_input("tot_bilirubin Value")
        direct_bilirubin=st.number_input("direct_bilirubin Value")
        tot_proteins=st.number_input("tot_proteins Value")
        albumin=st.number_input("albumin Value")
        ag_ratio=st.number_input("ag_ratio Value")
        sgpt=st.number_input("sgpt Value")
        sgot=st.number_input("sgot Value")
        alkphos=st.number_input("alkphos Value ")
        pred=""
          
        if st.button(" LIVER INFECTION CHEAKUP SYSTEM Result"):
            pred=Predictive_System([age,gender,tot_bilirubin,direct_bilirubin,tot_proteins,albumin,ag_ratio,sgpt,sgot,alkphos])
         
        st.success(pred)
    elif name.lower()=="stroke":
        st.title("STROKE PREDICTION MODEL")
        
        age =st.number_input("age of person")
        
        hypertension=st.text_input("hypertension level")
        heart_disease=st.text_input("heart_disease")
        avg_glucose_level=st.text_input("avg_glucose_level")
        bmi=st.text_input("BMI")
        Sex=st.text_input("SEX")
        Address=st.text_input("Address")
        Designation=st.text_input("Designation")
        Smoker=st.text_input("Smoker")
        Marriage=st.text_input("Marriage")
        
        diagonsis =''
        
        if st.button("Stroke Test Result"):
            diagonsis=stroke_predictive_system([age,hypertension,heart_disease,avg_glucose_level,bmi,Sex,Address,Designation,Smoker,Marriage ])
        
        st.success(diagonsis)
    elif name.lower()=="diabetes":
        st.title("DIABETES PREDICTION MODEL")
        
        
        Pregnancies=st.text_input("Number of Pregnancy")
        Glucose=st.text_input("Glucose Level")
        BloodPressure=st.text_input("BloodPressure")
        SkinThickness=st.text_input("SkinThickness")
        Insulin=st.text_input("Insulin Level")
        BMI=st.text_input("BMI value")
        DiabetesPedigreeFunction=st.text_input("DiabetesPedigreeFunction")
        Age=st.text_input("Age of Person")
        
        diagnosis =''
        
        if st.button("Diabetes Test Result"):
            diagnosis=diabetic_predictive_system([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
            
        
        
        st.success(diagnosis)


if __name__=="__main__":
    main()