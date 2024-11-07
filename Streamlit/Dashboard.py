import streamlit as st
import pandas as pd
import requests
import plotly.express as px

def format_number(value, prefix = ''):
  for unidade in ['', 'mil']:
    if value < 1000:
      return f'{prefix} {value:.2f} {unidade}'
    value /= 1000
    return f'{prefix} {value:.2f} milhões'
    

#Título
st.title("DASHBOARD DE VENDAS :shopping_trolley:")

url = 'https://labdados.com/produtos'
response = requests.get(url)

dados = pd.DataFrame.from_dict(response.json())

#Métrica
col1, col2 = st.columns(2)

with col1:
  st.metric("Receita", format_number(dados["Preço"].sum(), "R$"))
with col2:
  st.metric("Quantidade de vendas", format_number(dados.shape[0]))

#Tabela
st.dataframe(dados)
