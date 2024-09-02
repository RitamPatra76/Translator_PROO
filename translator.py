import streamlit as st
from transformers import pipeline
pipe = pipeline("translation", model="facebook/mbart-large-50-many-to-many-mmt")
language_codes = {
    "Bengali": "bn_IN",
    "Gujarati": "gu_IN",
    "Kannada": "kn_IN",
    "Telugu": "te_IN",
    "English": "en_XX"
}

st.title("Multilingual Translation App")
input_text = st.text_area("Enter text to translate:")
target_language = st.selectbox("Select target language:", options=list(language_codes.keys()))

if st.button("Translate"):
    if input_text:
        tgt_lang = language_codes[target_language]
        translated_text = pipe(input_text, src_lang="en_XX", tgt_lang=tgt_lang)[0]['translation_text']
        st.subheader("Translated Text:")
        st.write(translated_text)
    else:
        st.write("Please enter text to translate.")
