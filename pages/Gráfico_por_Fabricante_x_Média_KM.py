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
marca = st.sidebar.selectbox('Marca', sorted(data['make'].astype(str).unique()))

# Filtrar dados pela marca selecionada
dados_filtrados = data[data['make'].astype(str) == marca]

# Calcular a média de quilometragem por fabricante
media_quilometragem_por_fabricante = dados_filtrados.groupby('make')['mileage'].mean().reset_index()

# Criar um gráfico de barras com a média de quilometragem por fabricante
fig = px.bar(media_quilometragem_por_fabricante, x='make', y='mileage', title=f'Média de Quilometragem por Fabricante ({marca})')

# Exibir o gráfico
st.plotly_chart(fig)

# Créditos
st.sidebar.text("Desenvolvido por: Ayllen Aryelle")