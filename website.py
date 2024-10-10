import streamlit as st
from streamlit import image
from PIL import Image

st.header("GreenFoot🍃")
st.subheader("for a green future")

foot_img = image.open('foot_print_img.png')
st.image(foot_img)






