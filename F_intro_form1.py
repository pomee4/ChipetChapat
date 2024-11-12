"""
import streamlit as st
from PIL import Image

# Első kép megjelenítése
image1 = Image.open("./FORMS/INTRO_image/intro_1.jpg")
st.image(image1, use_container_width=True)

# Tovább gomb, egyedi kulccsal, ami beállítja az oldalt a session_state-ben
if st.button("Tovább", key="intro1_next"):
    st.session_state.page = './FORMS/intro_form2'
"""

import streamlit as st
from PIL import Image

def show_form1():
    # Első kép megjelenítése
    image1 = Image.open("./FORMS/INTRO_image/intro_1.jpg")
    st.image(image1, use_container_width=True)

    # Tovább gomb, ami beállítja az oldalt a session_state-ben
    if st.button("Tovább"):
        st.session_state.page = 'form2'