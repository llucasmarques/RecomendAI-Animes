import streamlit as st
from pipeline.pipeline import AnimePipeline
from dotenv import load_dotenv

st.set_page_config(page_title="Anime Recommender", layout="wide")
load_dotenv()

@st.cache_resource
def init_pipeline():
    return AnimePipeline()

pipeline = init_pipeline()

st.title("Anime Recommender Chat")
query = st.text_input("Enter your preference...")
if query:
    with st.spinner("Fetching animes for you..."):
        response = pipeline.recommend(query)
        st.write(response)