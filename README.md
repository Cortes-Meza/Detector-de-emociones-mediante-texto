# Detector de emociones mediante texto

Este proyecto de Machine learning clasifica frases en inglés según la emoción que expresan, utiliza procesamiento de lenguaje natural (NLP) y una interfaz interactiva sencilla con Streamlit para ejemplificar

## Objetivo

Detectar le emoción predominante de una frase, con emociones como:


- admiration
- amusement
- anger
- annoyance
- approval
- caring
- confusion
- curiosity
- desire
- disappointment
- disapproval
- disgust
- embarrassment
- excitement
- fear
- gratitude
- grief
- joy
- love
- nervousness
- optimism
- pride
- realization
- relief
- remorse
- sadness
- surprise
- neutral

## Dataset 

Se usó el conjunto de datos GoEmotions desarrolado por Google, el cuál, contiene más de 58,000 frases registradas con múltiples etiquetas emocionales.

Para este proyecto, se filtaron los ejemplos con una sola emoción para facilitar su clasificación.

## Librerías usadas

- pandas - Manipulación y análisis de datos estrucutrados.
- re - Expresiones regulares para limpieza de texto
- nltk - Procesamiento de lenguaje natural (tokenizació y steopwords)
- matplotlib y seaborn - Visualización de datos y métrics
- scikit-learn - Vectorización de texto (TF-IDF), modelos de clasificación y métricas de evaluación
-imbalanced-learn - Técnicas de sobremuestreo para balancear clases
- joblib - Serialización del modelo y vectorizador para reutilización
- Streamlit - Desarrollo de la interfaz web interactiva de la aplicación


