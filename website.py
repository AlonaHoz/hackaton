import streamlit as st
from streamlit import image
from PIL import Image

st.header("GreenFoot🍃")
st.subheader("for a green future")

world_img = Image.open('world_hand_img.webp')
st.image(world_img)






