#for comptetion in build. Joey,
#from team TDI-India, INDIA.
'''1-Create a program that analyses any random github repo and provides easy and quick explantion of code\n, 
with special reference to mathmatical logic behind code. 
2- Analyse the users metric, analyse how many times he asks ai and then gives a good rating,'''
#temp weblink wwww.getrightgit.com

"""use cases target - any coder , primary focus on PYTHON codes"""

import streamlit as st 
import os

import requests
import json
import openai
# from langchain.embeddings import OpenAIEmbeddings
# from openai.embeddings_utils import cosine_similarity
import os
import pandas



#step1 web app that has buttons 'my-github', "analyse code","my-problem-statement", "Ai Answer"


# Create a Streamlit app
st.title("Get the right Git-Repo! problem?")


    
# Add the button and text entry box to the app
b1 =st.button("my-problem")
l1=st.text_input("Tell us your problem", value="Describe clearly your problem")
b2=st.button("my-github")
l2=st.text_input("what github repo you want to use for solving above issue", value="provide link")
b3=st.button("analyze code")
l3=st.text_input("Solution to your problem", value="Ai suggestion")
b4=st.button("Ai answer")
#st.text_input("Ai Answers", value="Ai's Answer")

