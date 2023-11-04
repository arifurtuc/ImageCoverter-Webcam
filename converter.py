import streamlit as st
from PIL import Image
import io

st.subheader("Color to Grayscale Converter")

# Create a file uploader component allowing the user to upload a file
uploaded_image = st.file_uploader("Upload Image")

# Initialize variables to hold processed images
processed_image = None

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
        processed_image = gray_img

# Check if the image exists meaning the user has uploaded a file
if uploaded_image:
    # Open the user uploaded image with PIL
    img = Image.open(uploaded_image)

    # Convert the image to grayscale
    gray_uploaded_img = img.convert('L')

    # Display the grayscale image on the webpage
    st.image(gray_uploaded_img)
    processed_image = gray_uploaded_img

# Create a "Download Processed Image" button
if processed_image:
    processed_image_bytes = io.BytesIO()
    processed_image.save(processed_image_bytes, format="PNG")
    st.download_button(
        label="Download Processed Image",
        data=processed_image_bytes,
        key="download_button",
        file_name="processed_image.png",

    )

# Display a copyright using Markdown
st.markdown("&copy; 2023 Developed by Arif.")