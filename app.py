import streamlit as st
from src.utils.traducoes import translations
from src.utils.sidebar import custom_sidebar

custom_sidebar() # Custom sidebar function

# Initialize language
if 'lang' not in st.session_state:
    st.session_state.lang = 'en'

def toggle_language():
    st.session_state.lang = 'pt' if st.session_state.lang == 'en' else 'en'

lang = st.session_state.lang

# Define pages (each one already has its translated title)
pages = {
    '': [
        st.Page('form.py', title=translations[lang]['form_title']),
        st.Page('pages/about.py', title=translations[lang]['about_title']),
        st.Page('pages/credits.py', title=translations[lang]['credits_title']),
    ]
}

pg = st.navigation(pages)

# Layout: page title on the left + language button on the right
col1, col2 = st.columns([6, 2])
with col1:
    st.title(pg.title)  # open page title
with col2:
    st.button(translations[lang]['toggle'], on_click=toggle_language)

# Render the page
pg.run()
