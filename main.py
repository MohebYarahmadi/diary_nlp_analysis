import streamlit as st
import plotly.express as px
import glob
import functions

filepaths = glob.glob("data/*.txt")

st.set_page_config(page_title='Diary Analysis', layout='wide')
st.title('Diary Analysis using NLP')
st.subheader('You can see the diagrams here')

for filepath in filepaths:
    diary = functions.read_files(filepath)
    scores = functions.sentiment_analyzer(diary)
    print(filepath)
    print(scores)
    # figure = px.line(x=dates, y=pos, labels={'x': 'date', 'y': 'moode'})
    # st.plotly_chart(figure)
