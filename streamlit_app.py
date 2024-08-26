import streamlit as st
import pickle
import pandas as pd
import numpy as np

model=pickle.load(open('Linearmodel.1b','rb'))

df=pd.read_csv('salaryCleaned.xls')

st.title("Salary Predictor")
st.markdown("**A simple web app to predict salary**")


edu_list=df['Education Level'].unique()
job_list=df['Job Title'].unique()


age=st.number_input("Enter your age",value=None,placeholder="Type a number...")
edu=st.selectbox("Pick your education level",edu_list)
job_title=st.selectbox("Pick your job title",job_list)
experience=st.number_input("Enter your years of experience:",value=None,placeholder="Type a number...")

st.write('')
predict=st.button("Predict Salary")
st.write('')
st.write('')
st.write('')

if(predict):
    inp1=int(age)
    inp2=float(experience)
    inp3=int(np.where(edu_list==edu)[0][0])
    inp4=int(np.where(job_list==job_title)[0][0])

    X=[inp1,inp2,inp3,inp4]
    salary=model.predict([X])

    st.text(f"Estimated salary: ${int(salary[0])}")

