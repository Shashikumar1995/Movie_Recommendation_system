import pickle
import streamlit as st
import pandas as pd

movies = pickle.load(open('model/movie_list.pkl','rb'))
movies=pd.DataFrame(movies_list)

st.title('Movie Recommendation Syastem')


option = st.selectbox(
     'How would you like to be contacted?',
     ('Email', 'Home phone', 'Mobile phone'))
