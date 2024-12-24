import streamlit as st
import pandas as pd
import plotly.express as px

# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Crear el encabezado de la aplicación
st.header('Análisis de Vehículos Usados')

# Crear un botón para generar un histograma
hist_button = st.button('Construir histograma')

if hist_button:  # Cuando se hace clic en el botón
    # Mostrar un mensaje
    st.write('Generando un histograma para la columna "odometer"')

    # Crear un histograma usando plotly-express
    fig = px.histogram(car_data, x="odometer", title="Histograma de Odometer")
    
    # Mostrar el histograma en Streamlit
    st.plotly_chart(fig, use_container_width=True)
