import streamlit as st
import pandas as pd
import Levenshtein

# Cargar datos
datos = pd.read_excel('verbos1.xlsx')

u = pd.read_excel('verbos1.xlsx', sheet_name='inglés')
D_ingles = {str(español).strip().lower(): str(inglés).strip() for español, inglés in zip(u['Español'], u['Inglés'])}

ui = pd.read_excel('verbos1.xlsx', sheet_name='alemán')
D_aleman = {str(español).strip().lower(): str(alemán).strip() for español, alemán in zip(ui['Español'], ui['Alemán'])}

# Función para encontrar la palabra más cercana en el diccionario
def encontrar_palabra_cercana(palabra_usuario, diccionario):
    palabras_diccionario = diccionario.keys()
    distancias = [(palabra_diccionario, Levenshtein.distance(palabra_usuario, palabra_diccionario)) for palabra_diccionario in palabras_diccionario]
    palabra_cercana, distancia_minima = min(distancias, key=lambda x: x[1])
    return palabra_cercana, distancia_minima

# Streamlit App

st.markdown("<p style='color: blue; font-size: 32px; font-weight: bold;'>¡Traductor automático de textos! ✨</p>", unsafe_allow_html=True)

st.write("Este es un traductor automático de español al inglés y al alemán para el campo semántico de animales domésticos. Esperamos que te sea útil :)")

#Imagen de animales
#import streamlit as st
from PIL import Image  # Importar la clase Image de la biblioteca PIL (Python Imaging Library)

# Cargar la imagen
imagen = Image.open("animalesdomesticos.jpg")



# Mostrar la imagen en Streamlit

col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    st.image(imagen, caption="Te presentamos a los animales domésticos más lindos del mundo")
    # Redimensionar la imagen si es necesario
    imagen = imagen.resize((1000, 1000))
with col3:
    st.write(' ')

# Usuario elige la lengua de origen
lengua_origen = st.selectbox("Selecciona la lengua de origen:", ["Español", "Inglés", "Alemán"])

# Usuario ingresa una palabra en la lengua de origen
palabra_usuario = st.text_input(f"Ingresa una palabra en {lengua_origen}:")

# Convertir la palabra a minúsculas y quitar espacios adicionales
palabra_usuario = palabra_usuario.strip().lower()

# Mostrar traducciones en las otras dos lenguas
st.write("Traducciones:")

if lengua_origen == "Español":
    if palabra_usuario in D_ingles:
        st.write(f"- Inglés: {D_ingles[palabra_usuario]}")
    else:
        # Agregar corrección automática
        palabra_cercana, distancia = encontrar_palabra_cercana(palabra_usuario, D_ingles)
        if distancia <= 2:  # Puedes ajustar este umbral según tus necesidades
            st.write(f"- Inglés: Esta palabra no se encuentra en el diccionario. ¿Quisiste decir '{palabra_cercana}'?")
        
    if palabra_usuario in D_aleman:
        st.write(f"- Alemán: {D_aleman[palabra_usuario]}")
    else:
        # Agregar corrección automática
        palabra_cercana, distancia = encontrar_palabra_cercana(palabra_usuario, D_aleman)
        if distancia <= 2:  # Puedes ajustar este umbral según tus necesidades
            st.write(f"- Alemán: Esta palabra no se encuentra en el diccionario. ¿Quisiste decir '{palabra_cercana}'?")

elif lengua_origen == "Inglés":
    D_espanol = {str(inglés).strip().lower(): str(español).strip() for inglés, español in zip(u['Inglés'], u['Español'])}
    D_aleman = {str(inglés).strip().lower(): str(alemán).strip() for inglés, alemán in zip(u['Inglés'], ui['Alemán'])}

    if palabra_usuario in D_espanol:
        st.write(f"- Español: {D_espanol[palabra_usuario]}")
    else:
        # Agregar corrección automática
        palabra_cercana, distancia = encontrar_palabra_cercana(palabra_usuario, D_espanol)
        if distancia <= 2:  # Puedes ajustar este umbral según tus necesidades
            st.write(f"- Español: This word is not in the dictionary. Did you mean '{palabra_cercana}'?")
    
    if palabra_usuario in D_aleman:
        st.write(f"- Alemán: {D_aleman[palabra_usuario]}")
    else:
        # Agregar corrección automática
        palabra_cercana, distancia = encontrar_palabra_cercana(palabra_usuario, D_aleman)
        if distancia <= 2:  # Puedes ajustar este umbral según tus necesidades
            st.write(f"- Alemán: This word is not in the dictionary. Did you mean  '{palabra_cercana}'?")

elif lengua_origen == "Alemán":
    D_espanol = {str(alemán).strip().lower(): str(español).strip() for alemán, español in zip(ui['Alemán'], u['Español'])}
    D_ingles = {str(alemán).strip().lower(): str(inglés).strip() for alemán, inglés in zip(ui['Alemán'], u['Inglés'])}

    if palabra_usuario in D_espanol:
        st.write(f"- Español: {D_espanol[palabra_usuario]}")
    else:
        # Agregar corrección automática
        palabra_cercana, distancia = encontrar_palabra_cercana(palabra_usuario, D_espanol)
        if distancia <= 2:  # Puedes ajustar este umbral según tus necesidades
            st.write(f"- Español: Dieses Wort steht nicht in Wörterbuch. Hast du '{palabra_cercana}' gemeint?")
    
    if palabra_usuario in D_ingles:
        st.write(f"- Inglés: {D_ingles[palabra_usuario]}")
    else:
        # Agregar corrección automática
        palabra_cercana, distancia = encontrar_palabra_cercana(palabra_usuario, D_ingles)
        if distancia <= 2:  # Puedes ajustar este umbral según tus necesidades
            st.write(f"- Inglés: Dieses Wort steht nicht in Wörterbuch. Hast du '{palabra_cercana}' gemeint?")

