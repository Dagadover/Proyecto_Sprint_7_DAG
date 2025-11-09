import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

st.title('Visualización interactiva de vehículos')

st.write('Selecciona una o más opciones para visualizar los datos:')

# Crear casillas de verificación
show_hist = st.checkbox('Mostrar histograma de odómetro')
show_scatter = st.checkbox(
    'Mostrar diagrama de dispersión (odómetro vs precio)')

# Mostrar histograma
if show_hist:
    st.write('### Histograma del kilometraje de los vehículos')
    fig_hist = px.histogram(car_data, x='odometer',
                            nbins=30, title='Distribución del kilometraje')
    st.plotly_chart(fig_hist, use_container_width=True)

# Mostrar diagrama de dispersión
if show_scatter:
    st.write('### Diagrama de dispersión: Odómetro vs Precio')
    fig_scatter = px.scatter(
        car_data, x='odometer', y='price', title='Relación entre kilometraje y precio')
    st.plotly_chart(fig_scatter, use_container_width=True)
