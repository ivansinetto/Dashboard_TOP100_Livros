import streamlit as st
import pandas as pd
import plotly.express as px

# Estende o layout da tela até os cantos
st.set_page_config(layout="wide")

# Título
st.title('Dashboard')

# cada variável recebeu um arquivo CSV
df_reviews = pd.read_csv("datasets/customer reviews.csv")
df_top100_books = pd.read_csv("datasets/Top-100 Trending Books.csv")

# Cada variável recebeu a coluna de book price
price_max = df_top100_books["book price"].max() #Esse .max() procura o maior valor na coluna
price_min = df_top100_books["book price"].min() #Esse .min() procura o menor valor na coluna

# Variável com a sidebar 
max_price = st.sidebar.slider("Price Range", price_min, price_max, price_max) #Slider lateral (mínimo, máximo, de onde começa)

# variável com o filtro de preço condicional
df_books = df_top100_books[df_top100_books["book price"] <= max_price]

# Mostra o data-frame
df_books

# Variável com gráfico em barra filtrando o ano de publicação
fig = px.bar(df_books["year of publication"].value_counts()) #value_counts() é pra contar os números
fig2 = px.histogram(df_books["book price"])

# Cada variácel cria uma coluna
col1, col2 = st.columns(2)

# Mostra o gráfico 1 na coluna 1
col1.plotly_chart(fig)

# Mostra o gráfico 2 na coluna 2
col2.plotly_chart(fig2)