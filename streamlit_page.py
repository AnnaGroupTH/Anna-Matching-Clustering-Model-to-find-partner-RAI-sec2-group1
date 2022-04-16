import streamlit as st
import pandas as pd 
from clustering import simple_kmeans
from data_preprocessing import preprocessing_csv_to_df,add_user_info,drop_user_info,join_id_clts_and_sparing_df
import json


user_df = None 


def collect_user_info_page(): 

    # st.title('Welcome to AnnaMatching')
    # st.header("The Best platform to find your best partner")
    st.subheader("Please give us your information")

    user_email = st.text_input("Enter your Email", "6xxxxxx@kmitl.ac.th")
    user_name = st.text_input("Enter your Name-Surname")
    
    RAI_gen = st.radio('RAI Generation: ',
                    ('RAI 1  (Academic Year 2018)',
                    "RAI 2  (Academic Year 2019)",
                    "RAI 3  (Academic Year 2020)",
                    "RAI 4  (Academic Year 2021)",
                    "NANO(MATBOT) 1  (Academic Year 2020)",
                    "NANO(MATBOT) 2  (Academic Year 2021)",
                    'Other (Not RAI Engineering Student)'))


    Sex = st.radio('Sex: ',
                    ("Male",
                    "Female",
                    "LGBT+",
                    "Prefer not to say"))

    #-------------------------------------------------------------

    st.subheader("Your Personality")

    level4 = [None for i in range(4)]
    level4_topic = ["Focus of Attention","Information Input","Decision Making","Lifestyle"]
    level4_left = ["Extroversion","Observant","Thinking","Judgment"]
    level4_right = ["Introversion","Intuition","Feeling","Perception"]

    for i in range(4): 
        level4[i] = st.slider(fr"{level4_topic[i]}", 1, 5)
        st.text(fr"From {level4_left[i]}(1) to {level4_right[i]}(5)")
        st.text('Selected: {}'.format(level4[i]))

    #-------------------------------------------------------------

    st.subheader("Your Hardskills")

    level5 = [None for i in range(15)]
    level5_topic = ["Artificial Intelligence Engineering",
                    "Robotics Engineering ",
                    "Nanotechnology Engineering",
                    "Electronic Engineering",
                    "Cloud Computing",
                    "Analytical Reasoning",
                    "Data Science / Scientific Computing",
                    "Blockchain Developer",
                    "Game Developer",
                    "UX/UI Website Developer",
                    "Art / Graphic Design",
                    "Video Production",
                    "Sales",
                    "Business Analysis",
                    "Affiliate Marketing"]


    for i in range(15): 
        level5[i] = st.slider(fr"{level5_topic[i]}", 1, 5)
        st.text(fr"From Not at All(1) to Excellence(5)")
        st.text('Selected: {}'.format(level5[i]))
    #-------------------------------------------------------------

    st.subheader("Your Softskills")

    level6 = [None for i in range(8)]
    level6_topic = ["Leadership",
                    "Collaboration / Team Management",
                    "Time Management",
                    "Creative Thinking",
                    "Critical Thinking",
                    "Emotional Intelligence",
                    "Adaptability / Versatility",
                    "Negotiation / Conflict Resolution"]


    for i in range(8): 
        level6[i] = st.slider(fr"{level6_topic[i]}", 1, 5)
        st.text(fr"From Not at All(1) to Excellence(5)")
        st.text('Selected: {}'.format(level6[i]))

    #-------------------------------------------------------------

    st.subheader("Language")

    lang = ["Not at All","A1 (Beginner)","A2 (Elementary)",
                "B1 (Intermediate)","B2 (Upper Intermediate)","C1 (Advanced)",
                "C2 (Mastery)","Native Language"]

    thai_language = st.selectbox("Thai Language Skill: ", lang)
    english_language = st.selectbox("English Language Skill: ", lang)
    third_language = st.selectbox("The Third Language Skill: ", lang)

    next_page = st.button(label="Submit")

    if next_page == True:
        user_info = {'Email Address':user_email,
                        '1. Name-Surname':user_name,
                        '2. RAI Generation':RAI_gen,
                        '3. Sex':Sex,
                        '4.1 Focus of Attention':level4[0],
                        '4.2 Information Input':level4[1],
                        '4.3 Decision Making':level4[2],
                        '4.4 Lifestyle':level4[3],
                        '5.1 Artificial Intelligence Engineering':level5[0],
                        '5.2 Robotics Engineering':level5[1],
                        '5.3 Nanotechnology Engineering':level5[2],
                        '5.4 Electronic Engineering':level5[3],
                        '5.5 Cloud Computing':level5[4],
                        '5.6 Analytical Reasoning':level5[5],
                        '5.7 Data Science / Scientific Computing':level5[6],
                        '5.8 Blockchain Developer':level5[7],
                        '5.9 Game Developer':level5[8],
                        '5.10 UX/UI Website Developer':level5[9],
                        '5.11 Art / Graphic Design':level5[10],
                        '5.12 Video Production':level5[11],
                        '5.13 Sales':level5[12],
                        '5.14 Business Analysis':level5[13],
                        '5.15 Affiliate Marketing':level5[14],
                        '6.1 Leadership':level6[0],
                        '6.2 Collaboration / Team Management':level6[1],
                        '6.3 Time Management':level6[2],
                        '6.4 Creative Thinking':level6[3],
                        '6.5 Critical Thinking':level6[4],
                        '6.6 Emotional Intelligence':level6[5],
                        '6.7 Adaptability / Versatility':level6[6],
                        '6.8 Negotiation / Conflict Resolution':level6[7],
                        '7.1 Thai Language Skill':thai_language,
                        '7.2 English Language Skill':english_language,
                        '7.3 The Third Language Skill':third_language
                    }
        df = pd.DataFrame(user_info, index=[0])

        global user_df 
        user_df = df

        # show_data_page()


def show_data_page():

    # st.title('Anna Matching')
    # st.header("Here is your best partner")

    dataset_path = "C:/Users/soont/OneDrive/Desktop/H1/AnnaMatching2/Anna-Matching Survey (Responses).csv"


    training_df, sparing_df = preprocessing_csv_to_df(dataset_path)
    training_df = add_user_info(training_df,user_df)
    identified_clusters = simple_kmeans(training_df)
    df = join_id_clts_and_sparing_df(identified_clusters,sparing_df,save_csv=False)

    df = drop_user_info(df)

    st.dataframe(data=training_df)


if __name__ == "__main__":
    collect_user_info_page()
    show_data_page()
