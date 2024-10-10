import streamlit as st
from streamlit import image
from PIL import Image

st.header("GreenFoot🍃")
st.subheader("for a green future")

foot_print_img = Image.open('the_img.png')
st.image(foot_print_img, width=400)







