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
tipo_cambio = st.sidebar.selectbox('Tipo de Câmbio', sorted(data['gear'].astype(str).unique()))

# Filtrar dados pelo tipo de câmbio selecionado
dados_filtrados = data[data['gear'].astype(str) == tipo_cambio]

# Criar um gráfico de dispersão (scatter plot) com tipo de câmbio x potência em cavalos
fig = px.scatter(dados_filtrados, x='gear', y='hp', title=f'Relação entre Tipo de Câmbio e Potência em Cavalos ({tipo_cambio})')

# Exibir o gráfico
st.plotly_chart(fig)

# Créditos
st.sidebar.text("Desenvolvido por: Ayllen Aryelle")