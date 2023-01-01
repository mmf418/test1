import streamlit as st
from PIL import Image

st.title('Face recognition')

uploaded_file = st.file_uploader("Choose an image", type='jpeg')
if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption='Uploaded Image," ,use_columnwidth=True')