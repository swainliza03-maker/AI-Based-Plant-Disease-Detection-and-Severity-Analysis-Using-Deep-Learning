import streamlit as st

st.title(" Plant Disease Detection")

st.write(
    "AI-Based Plant Disease Detection and Severity Analysis "
    "Using Deep Learning"
)

st.info("Upload a plant leaf image to get a prediction.")

uploaded_file = st.file_uploader(
    "Upload Leaf Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    st.image(
        uploaded_file,
        caption="Uploaded Leaf Image",
        use_container_width=True
    )

    st.success("Image uploaded successfully!")
