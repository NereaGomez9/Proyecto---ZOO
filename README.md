# 🦁 ZOO – Clasificación de Animales mediante Machine Learning

## 📌 Descripción del proyecto
Este proyecto tiene como objetivo **clasificar el tipo de animal** a partir de sus **características físicas**, utilizando técnicas de *Machine Learning*.  
A partir de un conjunto de datos obtenido desde **Kaggle**, se entrenaron y compararon distintos modelos de clasificación para identificar cuál ofrece el mejor rendimiento.

El modelo que obtuvo los mejores resultados fue la **Regresión Logística**, alcanzando una **precisión del 96% (0.96)**.

---

## 📊 Dataset
- **Fuente:** Kaggle  
- **Formato:** CSV  
- **Descripción:**  
  El dataset contiene información sobre animales y sus características físicas (como número de patas, presencia de cola, tipo de respiración, etc.), junto con la clase o tipo de animal al que pertenecen.

---

## ⚙️ Metodología
1. Carga y exploración del dataset.
2. Limpieza y preparación de los datos.
3. Separación de variables independientes y variable objetivo.
4. División del conjunto de datos en entrenamiento y test.
5. Entrenamiento de distintos modelos de clasificación.
6. Comparación del rendimiento de los modelos.
7. Selección del modelo con mejor puntuación.

---

## 🤖 Modelos evaluados
Se entrenaron y compararon varios modelos de Machine Learning, entre ellos:
- Regresión Logística
- Otros modelos de clasificación

📌 **Resultado:**  
El modelo con mejor rendimiento fue la **Regresión Logística**, con una **accuracy de 0.96**, siendo el más adecuado para este problema de clasificación.

---

## 🏆 Resultados
- **Mejor modelo:** Regresión Logística  
- **Precisión (Accuracy):** 96%  
- **Objetivo alcanzado:**  
  Predecir correctamente el tipo de animal a partir de sus características físicas.

---

## 💻 Streamlit App
Se desarrolló una **aplicación interactiva en Streamlit** para que cualquier usuario pueda **predecir el tipo de animal introduciendo sus características físicas**:

- Archivo principal: `app.py`  
- Para ejecutarla localmente:

pip install -r requirements.txt ---
streamlit run app.py

La app permite introducir valores como:

- Número de patas
- Presencia de pelo, plumas o cola
- Si es acuático o terrestre
- Si es depredador, venenoso o doméstico
- Otros atributos físicos

Al hacer clic en **"Predecir"**, la app mostrará el tipo de animal predicho con un emoji representativo.

---

## 🛠️ Tecnologías utilizadas
- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Jupyter Notebook
- Streamlit

---

## 🚀 Conclusiones
Este proyecto demuestra que, a partir de características físicas simples, es posible **clasificar eficazmente distintos tipos de animales** utilizando modelos de Machine Learning.  
La Regresión Logística se mostró como una opción eficiente y precisa para este tipo de datos estructurados.  
Además, la app en Streamlit permite **interacción en tiempo real**, facilitando la visualización del resultado y la experimentación con diferentes combinaciones de características.

---

## 👩‍💻 Autora
**Nerea Gómez**  
Estudiante de Data Analytics / Data Science de Ironhack
