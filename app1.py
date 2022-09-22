
import pickle
import streamlit as st
pickle_in=open('Srija.pkl','rb')
model=pickle.load(pickle_in)
a=st.number_input('Enter NAME')
result=''

if st.predict('PREDICT'):
   result=st.predict([a])
   st.success(result)
