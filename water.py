import pickle 
import numpy as np
import streamlit as st

# load save model
model = pickle.load(open('waterQuality.sav', 'rb'))

# judul web
st.title('Prediksi Kualitas Air')

col1, col2, col3, col4 =st.columns(4)

with col1:
    alumunium = st.number_input('Alumunium')
with col2:
    ammonia = st.number_input('Ammonia')
with col3:
    arsenic = st.number_input('Arsenic')
with col4:
    barium = st.number_input('Barium')
with col1:
    cadmium = st.number_input('Cadmium')
with col2:
    chloramine = st.number_input('Chloramine')
with col3:
    chromium = st.number_input('Chromium:')
with col4:
    chopper = st.number_input('Chopper')
with col1:
    flouride = st.number_input('Flouride')
with col2:
    bacteria = st.number_input('Bacteria')
with col3:
    viruses = st.number_input('Viruses')
with col4:
    lead = st.number_input('Lead')
with col1:
    nitrates = st.number_input('Nitrates')
with col2:
    nitrites = st.number_input('Nitrites')
with col3:
    mercury = st.number_input('Mercury')
with col4:
    perchlorat = st.number_input('perchlorat')
with col1:
    radium = st.number_input('Radium')
with col2:
    selenium = st.number_input('Selenium')
with col3:
    silver = st.number_input('Silver')
with col4:
    uranium = st.number_input('Uranium')

# code for prediction
Kualitas_Air = ''

if st.button ('Prediksi Kualitas Air') :
    Kualitas_Air= model.predict([[alumunium, ammonia, arsenic, barium, cadmium, chloramine, chromium, chopper, flouride, bacteria, viruses, lead, nitrates, nitrites , mercury, perchlorat, radium, selenium, silver, uranium]])
    
    if (Kualitas_Air[0]==1):
        Kualitas_Air= 'Kualitas Air Aman'
    else:
        Kualitas_Air = 'Kualitas Air Tidak Aman'
        
st.success(Kualitas_Air)