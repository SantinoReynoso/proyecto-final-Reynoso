import streamlit as st
from openai import OpenAI
from env import API_KEY

client = OpenAI(API_KEY)

# Función para generar un chiste

def generar_chiste(palabra):
    # Generar chiste
    chiste = client.chat(palabra)
    # Mostrar chiste
    st.write(chiste)

    return chiste




def main():

    

    # titulo
    st.title("Generador de chistes")
    # instrucciones
    st.text("Instrucciones de uso:")
    st.text("1. Escribi una palabra")
    st.text("2. Presiona el botón")
    st.text("NUESTO ASISTENTE. Creará un chiste con tu palabra elegida")

    # chat
    # Entrada de usuario
    palabra = st.text_input("Ingrese una palabra para el chiste:")