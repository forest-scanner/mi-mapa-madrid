import streamlit as st
import pandas as pd
from keplergl import KeplerGl
from streamlit_keplergl import keplergl_static

# --- Configuración de la página ---
st.set_page_config(
    page_title="Mapa Interactivo de Madrid",
    page_icon="🗺️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Título y descripción
st.title("🗺️ Mapa Interactivo de Madrid con Kepler.gl")
st.markdown("""
Explora los principales puntos de interés de Madrid utilizando **Kepler.gl** para visualizaciones avanzadas.
""")

# --- Datos de Madrid ---
@st.cache_data
def cargar_datos_madrid():
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

# Configuración del mapa centrado en Madrid [citation:3]
config_madrid = {
    "version": "v1",
    "config": {
        "mapState": {
            "latitude": 40.4168,    # Centro de Madrid
            "longitude": -3.7038,   # Centro de Madrid
            "zoom": 12,
            "pitch": 0,
            "bearing": 0
        },
        "mapStyle": {
            "styleType": "dark"     # Puedes cambiar a "light" o "satellite"
        }
    }
}

# Sidebar con información
with st.sidebar:
    st.header("ℹ️ Información")
    st.markdown("""
    **Instrucciones:**
    - **Haz clic** en cualquier punto para ver información detallada
    - Usa el **zoom** para acercarte/alejarte
    - **Arrastra** para mover el mapa
    - Usa los controles de Kepler.gl para personalizar la visualización
    """)
    st.divider()
    st.markdown("### 📊 Datos del Mapa")
    st.metric("Puntos de interés", "13", "Madrid")

# --- Crear y mostrar el mapa usando Kepler.gl ---
datos_madrid = cargar_datos_madrid()

try:
    # Crear mapa de Kepler.gl [citation:4][citation:7]
    mapa = KeplerGl(height=600, config=config_madrid, show_docs=False)
    
    # Añadir datos al mapa [citation:3]
    mapa.add_data(data=datos_madrid, name='puntos_madrid')
    
    # Mostrar el mapa en Streamlit [citation:1][citation:4]
    keplergl_static(mapa)
    
except Exception as e:
    st.error(f"Error al cargar el mapa de Kepler.gl: {str(e)}")
    st.info("""
    Si hay errores, verifica que tengas instaladas las dependencias necesarias.
    Ejecuta: `pip install streamlit-keplergl keplergl pandas`
    """)

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
    "1. Explora el mapa interactivo de Madrid con Kepler.gl\n"
    "2. **Haz clic en los puntos** para ver información detallada\n"
    "3. Usa los controles avanzados de Kepler.gl para personalizar la visualización\n\n"
    "*Desarrollado con Streamlit + Kepler.gl*"
)


