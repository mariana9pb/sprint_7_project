import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
# crear un botón para histograma
hist_button = st.button('Construir histograma')
# crear un botón para gráfico de dispersión
disp_button = st.button('Construir gráfico de dispersión')

st.header('Car Data')

if hist_button:  # al hacer clic en el botón
    # escribir mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


if disp_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig_2 = px.scatter(car_data, x="odometer", y='price')

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_2, use_container_width=True)
