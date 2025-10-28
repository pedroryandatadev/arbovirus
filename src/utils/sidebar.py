import streamlit as st
import base64

def custom_sidebar():
    st.set_page_config( page_title='Arbovirus', page_icon='img/icon_4_alert.ico', layout='wide')
    
    # Loads the image and converts it to base64
    with open('img/arbovirus_bug_logo.png', 'rb') as f:
        logo_bytes = f.read()
    logo_base64 = base64.b64encode(logo_bytes).decode()

    # Inserts the image above the native menu and applies CSS
    st.markdown(
        f'''
        <style>
            /* Sidebar background color */
            [data-testid='stSidebar'] {{
                background-color: #262730;
                width: 290px !important;
            }}
            /* Setting to leave image at the top */
            [data-testid='stSidebar']::before {{
                content: '';
                display: block;
                background-image: url('data:image/png;base64,{logo_base64}');
                background-size: contain;
                background-repeat: no-repeat;
                background-position: center;
                height: 250px;
                margin-top: 150px;
            }}            
        </style>
        ''',
        unsafe_allow_html=True,
    )
