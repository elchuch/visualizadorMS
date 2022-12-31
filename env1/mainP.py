import folium as f
import pandas as pd
import  numpy as np
import seaborn as sns
import streamlit as st
from streamlit_folium import folium_static
import codecs
import streamlit.components.v1 as stc
def openHtml(chtml,width=800,height=1000):
    chtml=codecs.open(chtml,'r')
    ohtml=chtml.read()
    stc.html(ohtml,width=width,height=height,scrolling=False)
def createMap(dataframe,condition,color,s):
    df=dataframe
    c=condition
    m=f.Map(location=[19.47851, -99.23963],zoom_start=10,tiles=s)
    for i in range(len(df.index)):
        if c==df['PROBLEMATICA'][i]:
            popup=f.Popup("<strong>Escuela:</strong>{}<br>\n<strong>Descripción:</strong>{}<br>\n<strong>Ageb:</strong>{}".format(df.ESCUELA[i],df['DESCRIPCION '][i],df.AGEB[i])
                       ,max_width=250)
            f.Circle(location =[df.X[i],df.Y[i]],
            radius=50,
            popup=popup,
            color=color,
            fill=True,
            fill_opacity=0.9).add_to(m)
    return m





def main():
    df=pd.read_csv("data/3333.csv")
    menu=['Información','Mapa de denuncias']
    menuIn=['Paso peatonal','Rampas','Vandalismo','Seguridad','Luminarias','Señalización']
    col1,col2 = st.columns(2)
    with st.sidebar:
        st.image('images/logo1.jpeg','México social')
        choice=st.selectbox('Menu',menu)
    if choice == 'Mapa de denuncias':
        st.subheader("Denuncias  de FES-ACATLÁN")
        with col1:
            choice1=st.selectbox('Opciones',menuIn)
        with col2:
            choice2=st.radio('Cambiar mosaico',options=['OpenStreetMap','cartodb positron'])

        if choice1 == 'Paso peatonal':
            m1=createMap(df,'PASO PEATONAL','red',choice2)
            folium_static(m1,width=700,height=500)
        elif choice1== 'Rampas':
            m2=createMap(df,'RAMPA','green',choice2)
            folium_static(m2,width=700,height=500)
        elif choice1=='Vandalismo':
            m3=createMap(df,'VANDALISMO','blue',choice2)
            folium_static(m3,width=700,height=500)
        elif choice1== 'Seguridad':
            m4=createMap(df,'SEGURIDAD','black',choice2)
            folium_static(m4,width=700,height=500)
        elif choice1 == 'Luminarias':
            m5=createMap(df,'LUMINARIAS','black',choice2)
            folium_static(m5,width=700,height=500)
        elif choice1=='Señalización':
            m6=createMap(df,'SENALIZACION','black',choice2)
            folium_static(m6,width=700,height=500)
    else:
        openHtml("html/index.html")






if __name__=='__main__':
    main()