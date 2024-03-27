import streamlit as st
import pandas as pd

# Estende o layout da tela até os cantos
st.set_page_config(layout="wide")

# Título
st.header('Reviews de Livros')

# Cada variável recebeu um arquivo CSV
df_reviews = pd.read_csv("datasets/customer reviews.csv")
df_top100_books = pd.read_csv("datasets/Top-100 Trending Books.csv")

# Lista com nome dos livros
books = df_top100_books["book title"].unique() # Unique() pega todos os nomes únicos e corta as repetições

# Variável com a caixa de seleção de livros
book = st.sidebar.selectbox("Books", books) #(Nome, dataframe)

# Variável com o filtro de título condicional
df_book = df_top100_books[df_top100_books["book title"] == book]

# Variável com o filtro de título nas reviews condicional
df_reviews_f = df_reviews[df_reviews["book name"] == book]

# Variáveis com Título, Gênero, Preço, Rating e Ano de publicação
book_title = df_book["book title"].iloc[0] # iloc[] retira algo especificado no indice
book_genre = df_book["genre"].iloc[0]
book_price = f'${df_book["book price"].iloc[0]}'
book_rating = df_book["rating"].iloc[0]
book_year = df_book["year of publication"].iloc[0]

# Mostram título e gênero do livro selecionado
st.title(book_title)
st.subheader(book_genre)

# Cria colunas para cada variável
col1, col2, col3 = st.columns(3)

# Mostra Preço, Rating e Ano de publicação tabelados
col1.metric("Price", book_price)
col2.metric("Rating", book_rating)
col3.metric("Year of publication", book_year)

# Cria uma linha divisora
st.divider()

# Mostra os comentários do livro
for row in df_reviews_f.values:
    message = st.chat_message(f'{row[4]}')
    message.write(f'{row[2]}')
    message.write(f'{row[5]}')
