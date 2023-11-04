import streamlit as st
from PIL import Image

# Create an expander to start the camera
with st.expander("Start Camera"):
    # Capture an image from the camera input
    camera_image = st.camera_input("Camera")

# Check if an image was captured
if camera_image:
    # Open and process the captured image
    img = Image.open(camera_image)
    gray_img = img.convert("L")

    # Display the processed image
    st.image(gray_img)
