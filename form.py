import streamlit as st
import joblib
import pandas as pd
from src.utils.traducoes import translations

lang = st.session_state.lang

model = joblib.load('models/xgb_best_model.pkl')
label_encoder = joblib.load('models/label_encoder.pkl')

# Conteúdo da página inicial
st.write(translations[lang]['form_desc'])

with st.form('diagnosis_form'):

    st.subheader(translations[lang]['form_initial_text'])
    col1, col2 = st.columns(2)
    with col1:
        nu_idade = st.number_input(translations[lang]['form_age'], min_value=0, max_value=120, value=30)
    with col2:
        tp_sexo = st.selectbox(translations[lang]['form_sex'], translations[lang]['options_sex'])

    st.subheader(translations[lang]['form_symptoms'])

    col1, col2, col3 = st.columns(3)
    with col1:
        febre = st.selectbox(translations[lang]['form_fever'], translations[lang]['options_yes_no'])
        mialgia = st.selectbox(translations[lang]['form_mialgia'], translations[lang]['options_yes_no'])
        cefaleia = st.selectbox(translations[lang]['form_cefaleia'], translations[lang]['options_yes_no'])
    with col2:
        vomito = st.selectbox(translations[lang]['form_vomito'], translations[lang]['options_yes_no'])
        nausea = st.selectbox(translations[lang]['form_nausea'], translations[lang]['options_yes_no'])
        dor_costas = st.selectbox(translations[lang]['form_dor_costas'], translations[lang]['options_yes_no'])
    with col3:
        artralgia = st.selectbox(translations[lang]['form_artralgia'], translations[lang]['options_yes_no'])
        petequia_n = st.selectbox(translations[lang]['form_petequia_n'], translations[lang]['options_yes_no'])
        dor_retro = st.selectbox(translations[lang]['form_dor_retro'], translations[lang]['options_yes_no'])

    submitted = st.form_submit_button(translations[lang]['form_submit'])

# Fazer predição se enviar o formulário
if submitted:
    # Converter respostas 'Sim'/'Não' em 1/0
    sintomas = {
        'febre': 1 if febre == translations[lang]['options_yes_no'][1] else 0,
        'mialgia': 1 if mialgia == translations[lang]['options_yes_no'][1] else 0,
        'cefaleia': 1 if cefaleia == translations[lang]['options_yes_no'][1] else 0,
        'vomito': 1 if vomito == translations[lang]['options_yes_no'][1] else 0,
        'nausea': 1 if nausea == translations[lang]['options_yes_no'][1] else 0,
        'dor_costas': 1 if dor_costas == translations[lang]['options_yes_no'][1] else 0,
        'artralgia': 1 if artralgia == translations[lang]['options_yes_no'][1] else 0,
        'petequia_n': 1 if petequia_n == translations[lang]['options_yes_no'][1] else 0,
        'dor_retro': 1 if dor_retro == translations[lang]['options_yes_no'][1] else 0
    }

    # Converter sexo para número (igual ao usado no treino)
    tp_sexo_valor = 1 if tp_sexo == 'M' else 0

    # Montar dataframe de entrada com tipos numéricos
    X_input = pd.DataFrame([{
        'nu_idade': int(nu_idade),
        'tp_sexo': tp_sexo_valor,
        **sintomas
    }])

    # Garantir que tudo é numérico
    X_input = X_input.astype(float)

    # Fazer previsão
    y_pred = model.predict(X_input)
    class_name = label_encoder.inverse_transform(y_pred)[0]
    
    # Traduzir conforme o idioma atual
    translated_class = translations[lang]['disease_names'].get(class_name, class_name)

    st.markdown('---')
    st.subheader(translations[lang]['result_title'])
    st.success(f'**{translated_class}**')
    st.caption(translations[lang]['caption_mensenge'])