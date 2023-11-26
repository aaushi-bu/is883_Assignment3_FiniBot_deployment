# Import necessary libraries
import streamlit as st
import openai
import os
from io import StringIO
import pandas as pd

from langchain.document_loaders.csv_loader import CSVLoader
from langchain.chains import MultiPromptChain
from langchain.chains.router.llm_router import LLMRouterChain
from langchain.chains import ConversationChain
from langchain.llms import OpenAI
from langchain import PromptTemplate


# Make sure to add your OpenAI API key in the advanced settings of streamlit's deployment
open_AI_key = os.environ.get('OPENAI_API_KEY')
openai.api_key = open_AI_key

### Here, with some adjustments, copy-paste the code you developed for Question 1 in Assignment 3 
##########################################################################


##########################################################################


# UX goes here. You will have to encorporate some variables from the code above and make some tweaks.

st.header("Welcome to FiniBot!")
level = st.radio("Select your level:", ["Novice", "Expert"])

spectra = st.file_uploader("upload file", type={"csv", "txt"})
if spectra is not None:
    spectra_df = pd.read_csv(spectra)
st.write(spectra_df)
st.markdown(result)
