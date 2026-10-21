# --- Importar o Streamlit --- #
import streamlit as st

# --- Título da página --- #
st.title("Calculadora")

# --- Entrada dos números / number_input --- #
numero1= st.number_input(
    label="Digite o primeiro número",
    format="%0f"
)

numero2= st.number_input(
    label="Digite o segundo",
    format="%0f"
)

Resultado = None

Colunas = st.columns(2)

with Colunas[1]:

    if st.button(label="Multiplicação", use_container_width=True):
        Resultado = numero1 * numero2

    if st.button(label="Divisão", use_container_width=True):
        Resultado = numero1 / numero2

with Colunas[0]:

    if st.button(label="Soma", use_container_width=True):
        Resultado = numero1 + numero2

    if st.button(label="Subtração", use_container_width=True):
        Resultado = numero1 - numero2

if Resultado is not None:
    st.info(f"O Resultado é: {Resultado}")