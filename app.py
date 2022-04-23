import os
import streamlit as st
import numpy as np
from PIL import  Image

from multipage import MultiPage1,MultiPage2
from streamlit_page import collect_user_info_page, show_data_page, home_page


app1 = MultiPage1() 
app2 = MultiPage2()


display = Image.open('Logo.png')
st.image(display, width = 800)
st.title('Welcome to AnnaMatching')
st.header("The Best platform to find your best partner")

app1.add_page("Home_Page", home_page)
app1.add_page("Survey_Page", collect_user_info_page)
app2.add_page("Home_Page", show_data_page)

app1.run(app2)
