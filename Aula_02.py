#--- importa streamlit ---#
import streamlit as st

#--- Título da página ---#
st.title("Elementos interativos de Layout")

#--- Barra lateral ---#
st.sidebar.header("Opções da aplicação")
nome = st.sidebar.text_input(label="Dígite o seu nome")
st.sidebar.write(f"Olá, {nome}!")

#--- Colunas para organizar o conteúdo principal ---#
colunas = st.columns(2)

with colunas[0]:
    st.header("Interações simples")
    if st.button("Me aperte!"):
        st.success("Você clicou no botão!")

    valor_slider = st.slider(
        label="Selecione um valor",
        min_value=0,
        max_value=100,
        value=50
    )
    st.write(f"Valor do slider: {valor_slider}")

with colunas[1]:
    st.header("Irformações e imagens")
    st.info("Esta uma mensagem informativa")
    #--- Voce pode usar uma URL de imagem ou um caminho de um arquivo local ---#
    st.image(
       image="https://i.imgur.com/QLWTDhA.png",
       caption="Legenda da imagem",
       use_container_width=True,
    )
st.warning("Prerigo!") #AVISO!!!
st.image(
    image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSMlERB1KCr_ClybYMEjGEhjEo6EHiXrkCUGIHofppYVopFTdJfgNqjJmE&s=10"
)
st.error("ERROR!")

#--- Entrada de número e exibição ---#
numero= st.number_input(
    label="Digite um valor",
    min_value=0,
    max_value=100,
)
st.write(f"Seu valor é {numero}")