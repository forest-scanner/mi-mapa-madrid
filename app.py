import streamlit as st
import pandas as pd

# --- Configuración de la página ---
st.set_page_config(
    page_title="Mapa Interactivo de Madrid",
    page_icon="🗺️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Título y descripción
st.title("🗺️ Mapa Interactivo de Madrid")
st.markdown("""
Explora los principales puntos de interés de Madrid utilizando el mapa nativo de Streamlit.
""")

# --- Datos de Madrid ---
@st.cache_data
def cargar_datos_madrid():
    # Estructura de datos que contiene todos los puntos de interés de Madrid
    return pd.DataFrame({
        'nombre': [
            'Puerta del Sol', 'Palacio Real', 'Parque Retiro',
            'Plaza Mayor', 'Museo del Prado', 'Estadio Santiago Bernabéu',
            'Templo de Debod', 'Gran Vía', 'Museo Reina Sofía',
            'Puerta de Alcalá', 'Catedral de la Almudena',
            'Mercado de San Miguel', 'Jardines de Sabatini'
        ],
        'lat': [
            40.4169, 40.4179, 40.4150, 40.4155, 40.4138,
            40.4531, 40.4242, 40.4200, 40.4078, 40.4192, 40.4158,
            40.4153, 40.4185
        ],
        'lon': [
            -3.7034, -3.7142, -3.6830, -3.7074, -3.6921,
            -3.6883, -3.7176, -3.7050, -3.6945, -3.6932, -3.7144,
            -3.7095, -3.7138
        ],
        'tipo': [
            'Plaza', 'Monumento', 'Parque', 'Plaza', 'Museo',
            'Estadio', 'Monumento', 'Avenida', 'Museo', 'Monumento', 'Catedral',
            'Mercado', 'Jardines'
        ],
        'descripcion': [
            'Corazón de Madrid y kilómetro 0 de las carreteras españolas',
            'Residencia real oficial con más de 3.000 habitaciones',
            'Pulmón verde de Madrid con 125 hectáreas',
            'Plaza mayor histórica del siglo XVII',
            'Uno de los museos de arte más importantes del mundo',
            'Estadio del Real Madrid con capacidad para 81.044 espectadores',
            'Templo egipcio del siglo II a.C. donado a España',
            'Principal avenida comercial y de entretenimiento',
            'Museo de arte contemporáneo con el Guernica de Picasso',
            'Arco triunfal neoclásico del siglo XVIII',
            'Catedral de Madrid consagrada en 1993',
            'Mercado gourmet con especialidades españolas',
            'Jardines junto al Palacio Real con vistas espectaculares'
        ],
        'importancia': [5, 5, 4, 5, 5, 4, 3, 4, 5, 4, 4, 3, 3]
    })

# Sidebar con información
with st.sidebar:
    st.header("ℹ️ Información")
    st.markdown("""
    **Instrucciones:**
    - El mapa muestra los puntos de interés con un círculo.
    - Usa el **zoom** para acercarte/alejarte.
    - Consulta la tabla de abajo para la descripción detallada.
    """)
    st.divider()
    st.markdown("### 📊 Datos del Mapa")
    st.metric("Puntos de interés", "13", "Madrid")


# --- Crear y mostrar el mapa usando st.map() ---
datos_madrid = cargar_datos_madrid()

# Preparar los datos para st.map() renombrando las columnas
map_data = datos_madrid[['lat', 'lon']].copy()
map_data.columns = ['latitude', 'longitude'] 

# Mostrar el mapa, centrado en Madrid (zoom 12)
st.map(map_data, zoom=12, use_container_width=True)

# Información adicional debajo del mapa
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Puntos culturales", "5", "museos y monumentos")
with col2:
    st.metric("Espacios verdes", "2", "parques y jardines")
with col3:
    st.metric("Puntos emblemáticos", "6", "plazas y edificios")

st.divider()

# Mostrar los datos completos para el detalle de la descripción
with st.expander("Tabla de Puntos de Interés (Detalles de Descripción)"):
    st.dataframe(datos_madrid, use_container_width=True)

# Footer
st.divider()
st.markdown(
    "---\n"
    "### 📝 Cómo usar esta aplicación\n"
    "1. Explora el mapa interactivo de Madrid\n"
    "2. Usa los controles del mapa para navegar\n"
    "3. Consulta la tabla de abajo para ver la descripción de cada punto\n\n"
    "*Desarrollado con Streamlit nativo*"
)

