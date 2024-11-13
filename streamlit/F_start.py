"""
import streamlit as st
from FORMS import intro_form1, intro_form2, intro_form3, jump_form

# Beállítjuk az alapértelmezett oldalt, ha még nincs beállítva
if 'page' not in st.session_state:
    st.session_state.page = './FORMS/intro_form1'

# Váltás az oldalak között
if st.session_state.page == './FORMS/intro_form1':
    intro_form1
elif st.session_state.page == './FORMS/intro_form2':
    intro_form2
elif st.session_state.page == './FORMS/intro_form3':
    intro_form3
elif st.session_state.page == './FORMS/jump_form':
    jump_form
"""

import streamlit as st
from FORMS.intro_form1 import show_form1
from FORMS.intro_form2 import show_form2
from FORMS.intro_form3 import show_form3
from FORMS.jump_form import show_jump_form

# Alapértelmezett oldal beállítása, ha még nincs megadva
if 'page' not in st.session_state:
    st.session_state.page = 'form1'

# Váltás az oldalak között
if st.session_state.page == 'form1':
    show_form1()
elif st.session_state.page == 'form2':
    show_form2()
elif st.session_state.page == 'form3':
    show_form3()
elif st.session_state.page == 'jump_form':
    show_jump_form()