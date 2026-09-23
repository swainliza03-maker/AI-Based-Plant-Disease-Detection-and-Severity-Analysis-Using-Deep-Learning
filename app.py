import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
from huggingface_hub import hf_hub_download
from datasets import load_dataset
import cv2

st.set_page_config(
    page_title="Plant Disease Detection",
    page_icon="🌱"
)

st.title(" Plant Disease Detection")

st.write(
    "AI-Based Plant Disease Detection and Severity Analysis "
    "Using Deep Learning"
)


# Load disease class mapping
@st.cache_data
def load_class_mapping():

    dataset = load_dataset("geraldmc/plantvillage-tiny")

    class_mapping = {}

    for item in dataset["train"]:
        class_mapping[item["class_idx"]] = item["class_label"]

    return class_mapping


class_mapping = load_class_mapping()


# Load trained CNN model
@st.cache_resource
def load_model():

    model_path = hf_hub_download(
        repo_id="Liza-Swain/Plant-disease-model",
        filename="plant_disease_model (1).keras"
    )

    return tf.keras.models.load_model(model_path)


model = load_model()


# Upload image
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
    resized_image = image.resize((128, 128))

    # Convert to NumPy array
    image_array = np.array(resized_image).astype("float32") / 255.0

    # Add batch dimension
    image_input = np.expand_dims(image_array, axis=0)


    # Prediction
    prediction = model.predict(image_input)

    predicted_index = int(np.argmax(prediction[0]))

    confidence = float(
        np.max(prediction[0]) * 100
    )


    # Get disease name
    predicted_disease = class_mapping.get(
        predicted_index,
        f"Class {predicted_index}"
    )


    # Severity analysis
    image_uint8 = np.array(resized_image).astype(np.uint8)

    hsv_image = cv2.cvtColor(
        image_uint8,
        cv2.COLOR_RGB2HSV
    )

    gray_image = cv2.cvtColor(
        image_uint8,
        cv2.COLOR_RGB2GRAY
    )


    # Detect leaf area
    _, leaf_mask = cv2.threshold(
        gray_image,
        50,
        255,
        cv2.THRESH_BINARY
    )


    leaf_pixels = np.sum(
        leaf_mask > 0
    )


    # Detect possible diseased area
    disease_mask = (
        (hsv_image[:, :, 0] > 5) &
        (hsv_image[:, :, 0] < 45) &
        (hsv_image[:, :, 1] > 40)
    )


    affected_pixels = np.sum(
        disease_mask & (leaf_mask > 0)
    )


    if leaf_pixels > 0:

        affected_percentage = (
            affected_pixels / leaf_pixels
        ) * 100

    else:

        affected_percentage = 0


    # Severity level
    if affected_percentage < 20:

        severity = "Low"

    elif affected_percentage < 50:

        severity = "Moderate"

    else:

        severity = "Severe"


    # Display results
    st.subheader(" Prediction Result")

    st.success(
        f"🌿 Disease: {predicted_disease}"
    )

    st.info(
        f" Confidence: {confidence:.2f}%"
    )

    st.warning(
        f" Affected Area: {affected_percentage:.2f}%"
    )

    st.error(
        f" Severity Level: {severity}"
    )
