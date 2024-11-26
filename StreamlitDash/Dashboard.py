import streamlit as st
import pandas as pd
import requests
import plotly.express as px

st.set_page_config(layout= "wide")

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
dados["Data da Compra"] = pd.to_datetime(dados["Data da Compra"], format = "%d/%m/%Y")

###Tabelas
receita_estados = dados.groupby("Local da compra")["Preço"].sum()
receita_estados = dados.drop_duplicates(subset= "Local da compra")[["Local da compra", "lat", "lon"]].merge(receita_estados, left_on="Local da compra", right_index= True).sort_values("Preço", ascending=False)

receita_mensal = dados.set_index("Data da Compra").groupby(pd.Grouper(freq = "M"))["Preço"].sum().reset_index()
receita_mensal["Ano"] = receita_mensal["Data da Compra"].dt.year
receita_mensal["Mês"] = receita_mensal["Data da Compra"].dt.month_name()


## Gráficos
fig_mapa_receita = px.scatter_geo(receita_estados, 
                                  lat = 'lat',
                                  lon = "lon",
                                  scope= "south america",
                                  size = 'Preço',
                                  template="seaborn",
                                  hover_name="Local da compra",
                                  hover_data={"lat": False, "lon": False},
                                  title = "Receita por estado"
                                  )

fig_receita_mensal = px.line(receita_mensal,
                             x = 'Mês',
                             y = "Preço",
                             markers = True,
                             range_y = (0,receita_mensal.max()),
                             color = "Ano",
                             line_dash = "Ano",
                             title=  "Receita mensal")

fig_receita_mensal.update_layout(yaxis_title = "Receita")

##VIsualização no streamlit
#Métrica
col1, col2 = st.columns(2)

with col1:
  st.metric("Receita", format_number(dados["Preço"].sum(), "R$"))
  st.plotly_chart(fig_mapa_receita, use_container_width=True)
with col2:
  st.metric("Quantidade de vendas", format_number(dados.shape[0]))
  st.plotly_chart(fig_receita_mensal, use_container_width=True)

#Tabela
st.dataframe(dados)

#gráfico de mapa => precisa das coordenadas
#tabela mostrando a receita total por estados



