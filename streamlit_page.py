import streamlit as st
import pandas as pd 
from clustering import kmeans
from data_preprocessing import preprocessing_csv_to_df,add_user_info,drop_groups_info,join_id_clts_and_sparing_df, read_dataset


user_df = None 
user_email = None 
survey_done = None 
last_df = None 


def collect_user_info_page(): 

    placeholder = st.empty()
    with placeholder.container():
        st.write('If finished press button below the survey...')
        st.write('If you have not finished the survey...')
        st.write("--------------------------------------------------")
        st.write("--------------------------------------------------")
        st.subheader("Please give us your information")

        user_email = st.text_input("Enter your Email", "63xxxxxx")
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

        if RAI_gen == 0: thai_language = "NANO(MATBOT) 1  (Academic Year 2020)"
        if Sex == 0: thai_language = "Male"

        #-------------------------------------------------------------
        st.write("--------------------------------------------------")

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
        st.write("--------------------------------------------------")

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
        st.write("--------------------------------------------------")

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
        st.write("--------------------------------------------------")

        st.subheader("Language")

        lang = ["Not at All","A1 (Beginner)","A2 (Elementary)",
                    "B1 (Intermediate)","B2 (Upper Intermediate)","C1 (Advanced)",
                    "C2 (Mastery)","Native Language"]

        thai_language = st.selectbox("Thai Language Skill: ", lang)
        english_language = st.selectbox("English Language Skill: ", lang)
        third_language = st.selectbox("The Third Language Skill: ", lang)
        st.write("--------------------------------------------------")

        if thai_language == 0: thai_language = "Not at All"
        if english_language == 0: thai_language = "Not at All"
        if third_language == 0: thai_language = "Not at All"

        
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

        placeholder = st.empty()

        return user_df  


def show_data_page():

    dataset_path = "Anna-Matching Survey (Responses).csv"

    training_df0 = read_dataset(dataset_path)
    
    global user_email, survey_done
    if survey_done==False: training_df0 = add_user_info(training_df0,user_df)

    training_df, sparing_df = preprocessing_csv_to_df(training_df0)
    identified_clusters = kmeans(training_df)
    df = join_id_clts_and_sparing_df(identified_clusters,sparing_df,save_csv=False)

    df = drop_groups_info(df,user_email,survey_done)

    global last_df
    last_df = df 

    print(df)
    print(user_email)
    df = df.astype(str)
    st.dataframe(data=df)
    st.write("--------------------------------------------------")

    for i in range(len(df)):
        c = st.empty()
        with c.container():
            st.write("--------------------------------------------------")
            st.header("Information of person who you may like")
            info_list = df.iloc[i]
            info = lambda a,b : sum([int(x) for x in info_list[a:b]])/len([int(x) for x in info_list[a:b]])
            info_list = [info_list[1],info_list[2],info_list[3],info_list[4],
                                info(5,8),info(9,23),info(24,-4),
                                info_list[-3],info_list[-2],info_list[-1]]

            st.write('Email Address: ',info_list[0])
            st.write('Name-Surname: ',info_list[1])
            st.write('RAI Generation: ',info_list[2])
            st.write('Sex: ',info_list[3])

            st.subheader("Skill Score")
            st.write('score in range[0.00,5.00]')
            col1, col2, col3 = st.columns(3)
            col1.metric("Personality", "%.2f" %info_list[4])
            col2.metric("Hardskills", "%.2f" %info_list[5])
            col3.metric("Softskills", "%.2f" %info_list[6])

            st.subheader("Language skill")
            col1, col2, col3 = st.columns(3)

            for x in [-1,-2,-3]:
                if (info_list[x] == "Not at All"): info_list[x] = "Unable"
                elif (info_list[x] == "Native Language"): info_list[x] = "Native"
                else: info_list[x] = info_list[x][:2]

            col1.metric("Thai Language", info_list[-3])
            col2.metric("English Language", info_list[-2])
            col3.metric("Third Language", info_list[-1])

            st.write("--------------------------------------------------")


def home_page():
    with st.container():
        email = st.text_input('Your Email', '63xxxxxx')
        
        global user_email 
        user_email = email

        st.write('If you have done the survey already')
        agree = st.checkbox('YES')
        global survey_done
        survey_done = agree 

        return agree,email


if __name__ == "__main__":
    collect_user_info_page()
    show_data_page()
    home_page()
