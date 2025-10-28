import streamlit as st
from src.utils.traducoes import translations

lang = st.session_state.lang

st.write(translations[lang]['about_intro1'])
st.write(translations[lang]['about_intro2'])

st.write(translations[lang]['about_objective'])

st.subheader(translations[lang]['about_disease'])
st.write(translations[lang]['about_disease_intro'])
st.write(translations[lang]['about_disease_challenge'])
st.write(translations[lang]['about_dengue'])
st.write(translations[lang]['about_chikungunya'])
st.write(translations[lang]['about_other'])