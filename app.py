import streamlit as st
import pandas as pd
import sklearn
import pickle
pipe=pickle.load(open('gsc.pkl','rb'))
df=pickle.load(open('df.pkl','rb'))
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://wallpapercave.com/wp/wp8149661.jpg');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.title('Gold price prediction')
SPX=st.text_input('Enter s & p 500:')
GLD=st.text_input('Enter the price change in gold:')
USO=st.text_input('Enter the price of USO')
SLV=st.text_input('Enter iShares Silver Trust')

def make_prediction():
    input={
         'SPX':[SPX],
         'GLD':[GLD],
         'USO':[USO],
         'SLV':[SLV]
    }
    query=pd.DataFrame(input)
    prediction=pipe.predict(query)
    st.write(prediction)
    
if st.button('Prediction'):
    make_prediction()