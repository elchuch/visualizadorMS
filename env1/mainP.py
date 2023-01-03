import folium as f
import pandas as pd
import numpy as np
import seaborn as sns
import streamlit as st
from streamlit_folium import folium_static
import codecs
import streamlit.components.v1 as stc
import matplotlib.pyplot as plt


def openHtml(chtml, width=800, height=1000):
    chtml = codecs.open(chtml, 'r')
    ohtml = chtml.read()
    stc.html(ohtml, width=width, height=height, scrolling=False)


def createMap(dataframe, condition, color, s):
    df = dataframe
    c = condition
    m = f.Map(location=[19.47851, -99.23963], zoom_start=10, tiles=s)
    for i in range(len(df.index)):
        if c == df['PROBLEMATICA'][i]:
            popup = f.Popup("<strong>Escuela:</strong>{}<br>\n<strong>Descripción:</strong>{}<br>\n<strong>Ageb:</strong>{}".format(
                df.ESCUELA[i], df['DESCRIPCION '][i], df.AGEB[i]), max_width=250)
            f.Circle(location=[df.X[i], df.Y[i]],
                     radius=50,
                     popup=popup,
                     color=color,
                     fill=True,
                     fill_opacity=0.9).add_to(m)
    return m


def showData(data):
    fig, ax = plt.subplots(figsize=(8, 2))
    sns.countplot(data=data, x='PROBLEMATICA', ax=ax)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=75)
    ax.set_xlabel("Problematicas")
    ax.set_ylabel("Cantidad")
    ax.set_title("Datos recabados por alumnos de FES-ACATLÁN")
    return fig
def convert_df(data):
    return data.to_csv().encode('utf-8')


def main():
    df = pd.read_csv("data/3333.csv")
    menu = ['Información', 'Mapa de denuncias']
    menuIn = ['Paso peatonal', 'Rampas', 'Vandalismo',
              'Seguridad', 'Luminarias', 'Señalización','Opciones']
  
    col1, col2 = st.columns(2)
    with st.sidebar:
        st.image('images/logo1.jpeg', 'México social')
        choice = st.selectbox('Menu', menu)
    if choice == 'Mapa de denuncias':
        st.header("Denuncias  de FES-ACATLÁN")
        with col1:
            choice1 = st.selectbox('Selecciona', menuIn)
        with col2:
            choice2 = st.radio('Cambiar mosaico', options=[
                               'OpenStreetMap', 'cartodb positron'])
        
        if choice1 == 'Paso peatonal':
            m1 = createMap(df, 'PASO PEATONAL', 'red', choice2)
            folium_static(m1, width=700, height=500)
        elif choice1 == 'Rampas':
            m2 = createMap(df, 'RAMPA', 'green', choice2)
            folium_static(m2, width=700, height=500)
        elif choice1 == 'Vandalismo':
            m3 = createMap(df, 'VANDALISMO', 'blue', choice2)
            folium_static(m3, width=700, height=500)
        elif choice1 == 'Seguridad':
            m4 = createMap(df, 'SEGURIDAD', 'black', choice2)
            folium_static(m4, width=700, height=500)
        elif choice1 == 'Luminarias':
            m5 = createMap(df, 'LUMINARIAS', 'black', choice2)
            folium_static(m5, width=700, height=500)
        elif choice1 == 'Señalización':
            m6 = createMap(df, 'SENALIZACION', 'black', choice2)
            folium_static(m6, width=700, height=500)
        elif choice1== 'Opciones':
            if st.checkbox("Mostrar csv",False):st.write(df)
            if st.checkbox("Mostrar grafica",False):st.write(showData(df))
            if st.download_button(label="Descargar csv",
            data=convert_df(df),
            file_name='dataMexSocial.csv',
            mime='text/csv'

            ):st.markdown('DESCARGA EXITOSA')


    else:
        openHtml("html/index.html")
        
    


if __name__ == '__main__':
    main()
