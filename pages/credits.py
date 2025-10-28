import streamlit as st
from src.utils.traducoes import translations

lang = st.session_state.lang

st.subheader(translations[lang]['credits_developer'])
st.write('Pedro Ryan: https://github.com/pedroryandatadev')

st.subheader('Design')
st.write('Pedro Ryan: https://www.figma.com/@pedroryandev')

st.subheader(translations[lang]['credits_data_sources'])
st.write(translations[lang]['credits_data_gov'])

st.subheader(translations[lang]['credits_data_documentation'])
st.write(translations[lang]['credits_data_doc_gov'])