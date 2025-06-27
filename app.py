import streamlit as st
import joblib
import re 
import nltk

nltk.download('stopwords')

from nltk.corpus import stopwords

#Carga del modelo y vectorizador
model = joblib.load("modelo_emociones.pkl")
vectorizer = joblib.load("vectorizador_tfidf.pkl")
stop_words = set(stopwords.words('english'))

#Limpieza del texto
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)  # Eliminar puntuación
    tokens = text.split()
    tokens = [word for word in tokens if word not in stop_words]
    return " ".join(tokens)

st.set_page_config(page_title="Emotion detector")
st.title("Emotions detector in text")
st.write("Write a sentence and the model will detect the expressed emotion. ")

user_input = st.text_area("Your sentence: ")

if st.button("Detect Emotion"):
    if user_input.strip() == "":
        st.warning("Please enter a sentence. ")
    else:
        clean = clean_text(user_input)
        vec = vectorizer.transform([clean])
        prediction = model.predict(vec)[0]
        st.success(f"The emotion detected is:  **{prediction.upper()}**")