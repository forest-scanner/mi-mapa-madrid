import streamlit as st
from keplergl import KeplerGl
import pandas as pd
import streamlit.components.v1 as components

# Configuración de la página
st.set_page_config(
    page_title="Mapa Interactivo de Madrid",
    page_icon="🗺️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🗺️ Mapa Interactivo de Madrid con Kepler.gl")

# Datos de Madrid
datos_madrid = pd.DataFrame({
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

# Configuración del mapa
config_madrid = {
    "version": "v1",
    "config": {
        "mapState": {
            "latitude": 40.4168,
            "longitude": -3.7038,
            "zoom": 12
        }
    }
}

# Crear mapa
mapa = KeplerGl(height=600, config=config_madrid, show_docs=False)
mapa.add_data(data=datos_madrid, name='puntos_interes_madrid')

# Obtener el HTML
html_content = mapa._repr_html_()

# Si el contenido es bytes, lo decodificamos a string
if isinstance(html_content, bytes):
    html_content = html_content.decode('utf-8')

# Mostrar en Streamlit
components.html(html_content, height=600)




