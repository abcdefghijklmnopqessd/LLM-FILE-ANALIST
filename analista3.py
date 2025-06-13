# OBJETIVOS: criar um analista de dados com IA, que receba um arquivo .xlsx e analise-o de acordo com a mensagem do USer
from langchain_experimental.agents import create_pandas_dataframe_agent
import pandas as pd
from langchain_google_genai import GoogleGenerativeAI
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
import streamlit as st 

st.title("Analista de arquivos") 

uploaded_file = st.file_uploader("Escolha o arquivo: ")
pergunta_user = st.text_input("Coloque sua pergunta para ser realizada sobre o seu dataframe")
api_key = "AIzaSyD3omyfQGUY7HbRFiWUHoDPOypJvxG8njc"
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=api_key, temperature=0.2)

if uploaded_file is not None:
  dataframe = pd.read_excel(uploaded_file)


  agent_executor = create_pandas_dataframe_agent(
    llm,
    dataframe,
    verbose=True,
    return_intermediate_steps=True,
    allow_dangerous_code=True
  )
  try:
    resposta = agent_executor.invoke(pergunta_user)
    st.write(resposta)
    
  except Exception as e:
    st.error(f"Ocorreu um erro: {e}")
  