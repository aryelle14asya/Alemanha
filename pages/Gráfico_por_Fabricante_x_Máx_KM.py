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

# Criar um gráfico com o máximo de quilometragem por fabricante
fig = px.bar(dados_filtrados, x='make', y='mileage', title=f'Máximo de Quilometragem por Fabricante ({marca})')

# Exibir o gráfico
st.plotly_chart(fig)

# Créditos
st.sidebar.text("Desenvolvido por: Ayllen Aryelle")