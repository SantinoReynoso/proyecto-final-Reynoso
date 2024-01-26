import streamlit as st
from openai import OpenAI
import dotenv
import os

dotenv.load_dotenv()

# Configurar la clave de la API de OpenAI
openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=openai_api_key)


# Resto del código...

# Función para generar un chiste
def generar_chiste(palabra):
    prompt = f"Escribir un chiste sobre {palabra}"

    # Utilizar directamente openai_api_key
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    chiste = response.choices[0].message.content
    return chiste

def main():
    # título
    st.title("Generador de chistes")
    # instrucciones
    st.text("Instrucciones de uso:")
    st.text("1. Escribe una palabra")
    st.text("2. Presiona el botón")
    st.text("NUESTRO ASISTENTE. Creará un chiste con tu palabra elegida")

    # Entrada de usuario
    palabra = st.text_input("Ingrese una palabra para el chiste:", placeholder="Ingrese una palabra")
    if st.button("Generar chiste"):
        chiste = generar_chiste(palabra)
        st.write(chiste)

if __name__ == "__main__":
    main()
