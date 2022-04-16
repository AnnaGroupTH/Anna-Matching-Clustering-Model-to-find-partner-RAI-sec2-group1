import os
import streamlit as st
import numpy as np
from PIL import  Image

from multipage import MultiPage
from streamlit_page import collect_user_info_page, show_data_page


app = MultiPage()


def login_page():

    def check_password():

        def password_entered():
            if (
                st.session_state["username"] in st.secrets["passwords"]
                and st.session_state["password"]
                == st.secrets["passwords"][st.session_state["username"]]
            ):
                st.session_state["password_correct"] = True
                del st.session_state["password"]  
                del st.session_state["username"]
            else:
                st.session_state["password_correct"] = False

        if "password_correct" not in st.session_state:
            st.text_input("Username", on_change=password_entered, key="username")
            st.text_input(
                "Password", type="password", on_change=password_entered, key="password"
            )
            return False
        elif not st.session_state["password_correct"]:
            st.text_input("Username", on_change=password_entered, key="username")
            st.text_input(
                "Password", type="password", on_change=password_entered, key="password"
            )
            st.error("😕 User not known or password incorrect")
            return False
        else:
            return True

    if check_password():
        app.run()


display = Image.open('D:/data-storyteller-main/data-storyteller-main/Logo6.png')
st.image(display, width = 800)
st.title('Welcome to AnnaMatching')
st.header("The Best platform to find your best partner")

app.add_page("Survey_Page", collect_user_info_page)
app.add_page("Showingresult_Page", show_data_page)
# app.add_page("Login_Page", login_page)

login_page()
