import folium as f
import streamlit as st
from streamlit_folium import folium_static
import codecs
import streamlit.components.v1 as stc
import pandas as pd
import numpy as np

def openHtml(chtml,width=800,height=1000):
    cHtml=codecs.open(chtml,"r")
    oHtml=cHtml.read()
    stc.html(oHtml,width=width,height=height,scrolling=False)
def createMap(dataFrame):
    df=dataFrame
    m=f.Map(location=[19.47851, -99.23963],zoom_start=14) 
    for i,coordenada in enumerate(df.X):
       
       
        popup =f.Popup("<strong>Escuela:</strong>{}<br>\n<strong>Descripcion:</strong>{}<br>\n<strong>Ageb:</strong>{}".format(df.ESCUELA[i],df['DESCRIPCION '][i],df.AGEB[i])
                       ,max_width=250)
        f.Circle(location =[df.X[i],df.Y[i]],
            radius=30,
            popup=popup,
            color="crimson",
            fill=False).add_to(m)
       
    return  m
        
def main():
    path=r'data/dataFrameReportes.csv'
    df=pd.read_csv(path)
    
    
    menu=["Información","Mapa de denuncias"]
    menuDenuncia =["Alumnos","calles"]
   
    with st.sidebar:
        st.image('images/mexUnam.jpeg',"México social")
        choice=st.selectbox("Menú",menu)
        
    if choice == "Mapa de denuncias":
            st.subheader("DENUNCIAS HECHAS POR ALUMNOS DE FES ACATLAN") 
            choice1= st.selectbox("Selecciona",menuDenuncia)
           
            if choice1=='Alumnos':
                m1=createMap(df)
                folium_static(m1,width=700,height=500)
         
    else:
        st.subheader("México social")
        openHtml("html/index.html")     
   
if __name__=='__main__':
    main()