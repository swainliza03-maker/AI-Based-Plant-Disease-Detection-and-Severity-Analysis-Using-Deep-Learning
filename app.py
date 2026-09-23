import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

st.title(" Plant Disease Detection")

st.write(
    "AI-Based Plant Disease Detection and Severity Analysis "
    "Using Deep Learning"
)

# Load trained model from Hugging Face
MODEL_URL = "https://huggingface.co/Liza-Swain/Plant-disease-model/resolve/main/plant_disease_model%20%281%29.keras"

@st.cache_resource
def load_model():
    return tf.keras.models.load_model(MODEL_URL)

model = load_model()

uploaded_file = st.file_uploader(
    "Upload a plant leaf image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.image(
        image,
        caption="Uploaded Leaf Image",
        use_container_width=True
    )

    # Resize image
    image = image.resize((128, 128))

    # Convert to array
    image_array = np.array(image) / 255.0

    # Add batch dimension
    image_array = np.expand_dims(image_array, axis=0)

    # Prediction
    prediction = model.predict(image_array)

    predicted_class = np.argmax(prediction[0])
    confidence = np.max(prediction[0]) * 100

    st.success(f"Predicted Class: {predicted_class}")
    st.info(f"Confidence: {confidence:.2f}%")
