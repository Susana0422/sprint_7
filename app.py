import streamlit as st
import pandas as pd
import plotly.express as px

# Título de la aplicación
st.title('Análisis de Datos de Vehículos')

# Cargar los datos
@st.cache_data  # Usamos cache para evitar recargar los datos innecesariamente
def load_data():
    return pd.read_csv('vehicles_us.csv')

car_data = load_data()

# Mostrar los primeros registros de los datos
st.write(car_data.head())

# Botón para mostrar el histograma
if st.button('Mostrar Histograma'):
    # Crear un histograma
    fig_histogram = px.histogram(car_data, x="odometer", title="Histograma de Odometer")
    st.plotly_chart(fig_histogram)

# Botón para mostrar el gráfico de dispersión
if st.button('Mostrar Gráfico de Dispersión'):
    # Crear un gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Odometer vs Price")
    st.plotly_chart(fig_scatter)



