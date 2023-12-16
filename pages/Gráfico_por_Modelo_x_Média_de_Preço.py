import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar os dados
@st.cache_data
def load_data():
    data = pd.read_csv('Pasta1Sextou.csv', sep=';')
    return data

# Lê os dados
data = load_data()

# Inserir a logo do Carro
st.image('ram.png',  use_column_width=True)

# Adicionar filtros na barra lateral
st.sidebar.header('Filtros')
modelo = st.sidebar.selectbox('Modelo', sorted(data['model'].astype(str).unique()))

# Filtrar dados pelo modelo selecionado
dados_filtrados = data[data['model'].astype(str) == modelo]

# Calcular a média de preço por modelo
media_preco_por_modelo = dados_filtrados.groupby('model')['price'].mean().reset_index()

# Criar um gráfico de barras com a média de preço por modelo
fig = px.bar(media_preco_por_modelo, x='model', y='price', title=f'Média de Preço por Modelo ({modelo})')

# Exibir o gráfico
st.plotly_chart(fig)

# Créditos
st.sidebar.text("Desenvolvido por: Ayllen Aryelle")