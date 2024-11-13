"""
import streamlit as st
from PIL import Image

# Második kép megjelenítése
image2 = Image.open("./FORMS/INTRO_image/intro_2.jpg")
st.image(image2, use_container_width=True)

# Tovább gomb, egyedi kulccsal, ami beállítja az oldalt a session_state-ben
if st.button("Tovább", key="intro2_next"):
    st.session_state.page = './FORMS/intro_form3'
"""

import streamlit as st
from PIL import Image

def show_form2():
    # Második kép megjelenítése
    image2 = Image.open("./FORMS/INTRO_image/intro_2.jpg")
    st.image(image2, use_container_width=True)

    # Tovább gomb, ami beállítja az oldalt a session_state-ben
    if st.button("Tovább"):
        st.session_state.page = 'form3'