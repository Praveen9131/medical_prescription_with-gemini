import streamlit as st
from PIL import Image
import google.generativeai as genai

# Replace with your actual API key
#apiKey = "AIzaSyBIQSIK7DQzWmaB3fr78b-OO_KRbaZITgM"

# Configure Gemini-Pro Vision model
#genai.configure(api_key=apiKey)
from dotenv import load_dotenv
import os
  # Assuming this is your library for Gemini-Pro Vision

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
apiKey = os.getenv("GENAI_API_KEY")

# Configure Gemini-Pro Vision model
genai.configure(api_key=apiKey)

model = genai.GenerativeModel('gemini-pro-vision')

def generate_prescription(image):
    response = model.generate_content(["Write a prescription in pointer format ordered by name of medicine, symptoms, primary diagnosis, usage and dosage and manufacture and expire date of the medicine of medicine in the image. Make sure to ask person to visit doctor if problem persists.", image])
    return response.text

# Streamlit interface code
st.title('Medicine Prescription Generator')
st.write('Upload an image and get a prescription.')

uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    if st.button('Generate Prescription'):
        prescription = generate_prescription(image)
        st.markdown(f"**Prescription:**\n{prescription}")

st.write('---')
st.write('**Note:** This application uses Google Gemini-Pro Vision for generating prescriptions based on uploaded images.')
