import streamlit as st

# Inserir a logo do Spotify
st.image('ram.png', use_column_width=True)

# Centralizar o título do dashboard
st.markdown("<h1 style='text-align: center;'>Conjunto de dados de carros da Alemanha</h1>", unsafe_allow_html=True)

# Apresentação do estudo
st.title("Conjunto de dados extraído do AutoScout24 com informações sobre carros novos e usados.")

st.write("Este Conjuto de dados analisa informações sobre marcas, modelos de carros, cambio, ano, preços e quilometragem.")
st.write("características que descrevem 46.405 veículos à venda na Alemanha, com ano de registro de 2011 a 2021")

st.subheader("Dicionário de Dados")

tabela_markdown = """
| Variável    | Classe    | Descrição                                     |
|-------------|-----------|-----------------------------------------------|
| Mileage     | character | Quilometragem                                 |
| Make        | character | Fabricante                                    |
| Model       | character | Modelo do Carro                               |
| Fuel        | character | Combustível                                   |
| Gear        | character | Engrenagem do Carro                           |
| OffType     | character | Tipo de oferta do carro                       |
| Price       | character | Preço do Carro                                |
| Hp          | character | Potência de Cavalo                            |
| Year        | character | Ano do Carro                                  |
"""

# Usando st.write para exibir a tabela Markdown
st.write(tabela_markdown)

# Apresentação das principais análises realizadas
st.subheader("Principais Análises Realizadas:")
st.markdown("""
- **Análise de Quilometragem:** Analisar a Quilometragem de carros mencionados no filtro.
- **Análise de Fabricante:** Demonstração de cada Fabricante dos modelos dos carros.
- **Análise por Modelo de Carro:** Análise e visualização de cada Modelo de Carro.
- **Combustível do Carro:** Visualização do Combustível de cada carro.
- **Engrenagem do Carro:** Mostrar se é um carro automático ou manual.
- **Tipo de Oferta do Carro:** Quais serão as ofertas de cada carro.
- **Preço do Carro:** Mostrar os preços do carro de acordo com o modelo/fabricante/ano/combustível/km.
- **Potência de Cavalo:** Visualizar a potência do motor de cada carro.
- **Ano do Carro:** Mostrar o ano em que o carro foi fabricado.
""")

# Créditos
st.sidebar.text("Desenvolvido por: Ayllen Aryelle")
