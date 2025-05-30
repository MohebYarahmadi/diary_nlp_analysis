import streamlit as st
import plotly.express as px
import glob
import functions

filepaths = sorted(glob.glob("data/*.txt"))
dates = functions.get_dates(filepaths)
pos_scores = []
neg_scores = []

st.set_page_config(page_title='Diary Tone')
st.title('Diary Tone')
st.subheader('NLP Analysis')

for filepath in filepaths:
    diary = functions.read_files(filepath)
    scores = functions.sentiment_analyzer(diary)
    pos_scores.append(scores['pos'])
    neg_scores.append(scores['neg'])


st.subheader("Positivity")
pos_figure = px.line(x=dates, y=pos_scores, labels={'x': 'Date', 'y': 'Positivity'})
st.plotly_chart(pos_figure)

st.subheader("Negativity")
neg_figure = px.line(x=dates, y=neg_scores, labels={'x': 'Date', 'y': 'Negativity'})
st.plotly_chart(neg_figure)
