##Health Management APP from dotenv 
from dotenv import load_dotenv 
load_dotenv()  # load all the environment variables
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

st.set_page_config(page_title="Gemini Decode: Multilanguage Document Extraction by Gemini Pro")

# Initialize Streamlit app
st.header("Gemini Decode: Multilanguage Document Extraction by Gemini Pro")
text = "Utilizing the Gemini Pro AI, this project effortlessly extracts vital information  \
from diverse multilingual documents, transcending language barriers with precision and  \
efficiency for enhanced productivity and decision-making."
styled_text = f"<span style='font-family:serif;'>{text}</span>"
st.markdown(styled_text, unsafe_allow_html=True)

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Google Gemini Pro Vision API and get response
def get_gemini_response(input_text, image, prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([input_text, image, prompt])
    return response.text

uploaded_file = st.file_uploader("Choose an image of the document:", type=["jpg", "jpeg", "png"])
image = None
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_container_width=True)

question = st.text_input("Ask any questions about the document:")

submit = st.button("Tell me about the document")

input_prompt = """
You are an expert in understanding text in any language and decode them.
We will upload any image of either the document or images of anything and you will have to describe the image and you will have to answer any questions based on the uploaded Image.
"""

# Function to process the uploaded image
def input_image_details(uploaded_file):
    image = Image.open(uploaded_file)
    return image

# If the user clicks the submit button
if submit and uploaded_file is not None:
    image_data = input_image_details(uploaded_file)
    if question:
        response = get_gemini_response(question, image_data, input_prompt)
    else:
        response = get_gemini_response("Describe the document.", image_data, input_prompt)
    st.subheader("The response is")
    st.write(response)
else:
    st.write("Please upload an image and click the button to get the document analysis.")