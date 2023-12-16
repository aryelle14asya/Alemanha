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
combustivel = st.sidebar.selectbox('Tipo de Combustível', sorted(data['fuel'].astype(str).unique()))
transmissao = st.sidebar.selectbox('Transmissão', sorted(data['gear'].astype(str).unique()))
ano_veiculo = st.sidebar.slider('Ano do Veículo', min_value=int(data['year'].min()), max_value=int(data['year'].max()))
tipo_oferta = st.sidebar.selectbox('Tipo de Oferta', sorted(data['offerType'].astype(str).unique()))

# Aplicar filtros aos dados
dados_filtrados = data[
    (data['make'].astype(str) == marca) &
    (data['fuel'].astype(str) == combustivel) &
    (data['gear'].astype(str) == transmissao) &
    (data['year'] == ano_veiculo) &  # Não é necessário converter 'year', pois já é int
    (data['offerType'].astype(str) == tipo_oferta)
]

# Exibir os dados filtrados
st.write('**Dados Filtrados**')
st.table(dados_filtrados)

# Créditos
st.sidebar.text("Desenvolvido por: Ayllen Aryelle")