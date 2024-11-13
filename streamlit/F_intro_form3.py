import streamlit as st
from PIL import Image

def show_form3():
    # Harmadik kép megjelenítése
    image3 = Image.open("./FORMS/INTRO_image/intro_3.jpg")
    st.image(image3, use_container_width=True)

    # Szövegbuborék és gomb hozzáadása
    st.markdown("""
        <div style="position: relative; width: 100%; text-align: left;">
            <!-- Szövegbuborék elem -->
            <div style="
                position: absolute;
                bottom: 350px;
                left: 455px;
                box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.3);
                width: 200px;
                text-align: center;
                font-family: Arial, sans-serif;
            ">
                <p style="font-size: 18px; margin: 0; color:black;">A KSH adataiból nézünk fogyasztási adatokat?</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Igen gomb, egyedi kulccsal
    if st.button("Igen, megnézem!", key="intro3_next"):
        st.session_state.page = 'jump_form'