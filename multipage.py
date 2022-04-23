import streamlit as st
import pandas as pd 
import time


class MultiPage(object):
    def __init__(self) -> None:
        self.pages = []
        self.num = 0

    def add_page(self, title, func) -> None: 

        self.pages.append({
                "title": title, 
                "function": func
            })


class MultiPage1(MultiPage): 

    def __init__(self) -> None:
        self.pages = []
        self.num = 0

    def run(self,app):
        placeholder1 = st.empty()
        with placeholder1.container():
            x,email = self.pages[0]["function"]()
            z = self.pages[1]["function"]()
            y = st.button('Submit')
        if y:
            placeholder1.empty()
            if x==True:
                dataset_path = "C:/Users/soont/OneDrive/Desktop/H1/AnnaMatching/Anna-Matching Survey (Responses).csv"
                df = pd.read_csv(dataset_path)
                if fr"{email}" in list(df["Email Address"]):
                    print(z)
                    app.run()
                else: 
                    st.error("😕 User Email unfound!!!!")
                    # time.sleep(5)
                    # self.run(app)
            else: 
                print(z)
                app.run()


class MultiPage2(MultiPage): 

    def __init__(self) -> None:
        self.pages = []
        self.num = 0


    def run(self):
        page = st.sidebar.selectbox(
            'App Navigation', 
            self.pages, 
            format_func=lambda page: page['title']
        )
        page['function']()