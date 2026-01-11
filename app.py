import streamlit as st
import pandas as pd
import joblib

# Cargar objetos entrenados
model = joblib.load("models/best_model.pkl")
scaler = joblib.load("models/scaler.pkl")
columns = joblib.load("models/columns.pkl")

st.set_page_config(page_title="ZOO Classifier", page_icon="🦁")

st.title("🦁 Clasificador de Animales - ZOO")
st.write("Introduce las características físicas del animal:")

# Inputs
hair = st.selectbox("¿Tiene pelo?", [0, 1])
feathers = st.selectbox("¿Tiene plumas?", [0, 1])
eggs = st.selectbox("¿Pone huevos?", [0, 1])
milk = st.selectbox("¿Produce leche?", [0, 1])
airborne = st.selectbox("¿Vuela?", [0, 1])
aquatic = st.selectbox("¿Es acuático?", [0, 1])
predator = st.selectbox("¿Es depredador?", [0, 1])
toothed = st.selectbox("¿Tiene dientes?", [0, 1])
backbone = st.selectbox("¿Tiene columna vertebral?", [0, 1])
breathes = st.selectbox("¿Respira aire?", [0, 1])
venomous = st.selectbox("¿Es venenoso?", [0, 1])
fins = st.selectbox("¿Tiene aletas?", [0, 1])
legs = st.slider("Número de patas", 0, 8, 4)
tail = st.selectbox("¿Tiene cola?", [0, 1])
domestic = st.selectbox("¿Es doméstico?", [0, 1])
catsize = st.selectbox("¿Tamaño similar a un gato?", [0, 1])

if st.button("🔍 Predecir"):
    nuevo_prueba = pd.DataFrame([{
        'hair': hair,
        'feathers': feathers,
        'eggs': eggs,
        'milk': milk,
        'airborne': airborne,
        'aquatic': aquatic,
        'predator': predator,
        'toothed': toothed,
        'backbone': backbone,
        'breathes': breathes,
        'venomous': venomous,
        'fins': fins,
        'legs': legs,
        'tail': tail,
        'domestic': domestic,
        'catsize': catsize
    }])

    # MISMA lógica que tu notebook
    nuevo_prueba = nuevo_prueba[columns]
    nuevo_prueba_scaled = scaler.transform(nuevo_prueba)
    pred = model.predict(nuevo_prueba_scaled)

    st.success(f"🐾 Tipo de animal predicho: **{pred[0]}**")
