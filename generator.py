import streamlit as st
import openai
from PIL import Image
import requests
from io import BytesIO

openai.api_key = 'YOUR OPENAI KEY'

#input 2 dinosaurs
st.title('Unveiling the Unseen - The Dinosaur Breeding Ground')
dino1_name = st.text_input('Enter the first dinosaur name:')
dino2_name = st.text_input('Enter the second dinosaur name:')

#send prompt to open ai api
if st.button('Generate Hybrid Dinosaur'):
    prompt = f"Let's assume that a {dino1_name} and {dino2_name} bred together to have a baby dinosaur." \
        " This baby dinosaur then grew up and is now a big dinosaur. What would it look like?" \
        " If one of the dinosaurs has wings, include them in the image. Please emphasize" \
        " the wings, horns, and such distinct features in the child. Should be an animated image. No text" \
        " should be present in the image."

    response = openai.Image.create(
        prompt=prompt,
        n=1,  # Number of images to generate
        size="1024x1024"  # Size of the generated images
    )
    
    #extract and present image
    image_url = response['data'][0]['url']
    image_response = requests.get(image_url)
    image = Image.open(BytesIO(image_response.content))
    st.image(image, caption='Hybrid Dinosaur')
