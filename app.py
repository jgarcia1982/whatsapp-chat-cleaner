import streamlit as st
import re

# Función para limpiar el chat
def limpiar_chat(contenido):
    lineas_limpiadas = []
    patron = r"^.*? - "

    # Procesar cada línea del contenido
    for linea in contenido.splitlines():
        linea_limpiada = re.sub(patron, "", linea)
        lineas_limpiadas.append(linea_limpiada.strip())
    
    # Unir las líneas limpiadas
    return "\n".join(lineas_limpiadas)

# Interfaz de Streamlit
st.title("Limpieza de Chats de WhatsApp")

# Cargar archivo
archivo_subido = st.file_uploader("Sube un archivo de chat .txt", type="txt")

if archivo_subido:
    # Leer el contenido del archivo
    contenido = archivo_subido.read().decode("utf-8")
    
    # Limpiar el chat
    chat_limpiado = limpiar_chat(contenido)

    # Mostrar resultado
    st.subheader("Chat Limpiado:")
    st.text_area("Contenido del Chat", chat_limpiado, height=300)

    # Botón para descargar el chat limpiado
    st.download_button(
        label="Descargar Chat Limpiado",
        data=chat_limpiado,
        file_name="chat_limpiado.txt",
        mime="text/plain"
    )
