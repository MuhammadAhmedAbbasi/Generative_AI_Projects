from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
from dotenv import load_dotenv


load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACKING_V2"]="true"



# PromtTemplate

promt=ChatPromptTemplate.from_messages(
    [
        ("system","You are helpul researcher who is expert in EEG,ECG PPG, please respond to the queries"),
        ("user","Question:{question}")

    ]

)

# StreamLit

st.title('ECG, EEG, EXPERT RESEARCHER HELPER')
input_text=st.text_input("Search the topic you want")

# openAI LLm
llm=ChatOpenAI(model="gpt-3.5-turbo")
output_parser=StrOutputParser()
chain=promt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))