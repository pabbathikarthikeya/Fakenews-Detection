import streamlit as st
import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

model=pickle.load(open('model.pkl','rb'))
vectorize=pickle.load(open('vectorize.pkl','rb'))
st.title("Fake news Detector")

news=st.text_area("Enter news artical")
if st.button('predict'):
    vec=vectorize.transform([news])
    pred=model.predict(vec)
    st.success("This news is Real" if pred[0]=="Real" else "This news is Fake")
    
