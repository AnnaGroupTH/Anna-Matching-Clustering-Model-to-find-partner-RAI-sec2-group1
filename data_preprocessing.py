import pandas as pd
import numpy as np 


def preprocessing(df):

    #string to int for column <2. RAI Generation>
    rai = ["RAI 1  (Academic Year 2018)",
        "RAI 2  (Academic Year 2019)",
        "RAI 3  (Academic Year 2020)",
        "RAI 4  (Academic Year 2021)",
        "NANO(MATBOT) 1  (Academic Year 2020)",
        "NANO(MATBOT) 2  (Academic Year 2021)"]

    num = 0
    for x in rai:
        df.loc[df['2. RAI Generation'] == x , "2. RAI Generation"] = num
        num += 1


    #string to int for column <3. Sex>
    sex = ["Male","Female","LGBT+","Prefer not to say"]

    num = 0
    for i in sex:
        df.loc[df['3. Sex'] == i , "3. Sex"] = num
        num += 1


    #string to int for columns <7. language>
    lang = ["Not at All","A1 (Beginner)","A2 (Elementary)",
            "B1 (Intermediate)","B2 (Upper Intermediate)","C1 (Advanced)",
            "C2 (Mastery)","Native Language"]

    num = 0
    for i in lang:
        df.loc[df['7.1 Thai Language Skill'] == i , "7.1 Thai Language Skill"] = num
        df.loc[df['7.2 English Language Skill'] == i , "7.2 English Language Skill"] = num
        df.loc[df['7.3 The Third Language Skill'] == i , "7.3 The Third Language Skill"] = num
        num += 1

    return df 


def preprocessing_csv_to_df(dataset_path):


    # reading csv or excel -> DataFrame
    if ".xlsx" in dataset_path:
        df = pd.DataFrame(pd.read_excel(dataset_path))

    elif ".csv" in dataset_path: 
        df = pd.read_csv(dataset_path)

    else: print("Please check file format!")


    # sparing df 
    df1 = df.copy()
    df2 = df.copy()


    # dropping 
    del_col = ["Timestamp","Email Address","1. Name-Surname"]
    df1 = df1.drop(del_col , axis = 1)
    df2 = df2.drop(["Timestamp"], axis=1)


    df1 = preprocessing(df1)

    return df1,df2


def add_user_info(df,user_df):

    del_col = ["Email Address","1. Name-Surname"]
    user_df = user_df.drop(del_col , axis = 1)
    user_df = preprocessing(user_df)
    df = df.append(user_df, ignore_index = True)
    
    return df 


def drop_user_info(df): 

    df = df.loc[df['group'] == df["group"][len(df)-1]]
    # df = df.loc[df['group'] == df["group"][len(df)-1]]
    # df = df.loc[df['group'] == 4]
    # df = df[:][:len(df)-1]

    return df 


def join_id_clts_and_sparing_df(identified_clusters,sparing_df,save_csv=False):
    
    # print(len(identified_clusters))
    # print(type(identified_clusters))
    y_df = pd.DataFrame(identified_clusters, columns=["group"])
    # y_df.rename(columns={"0","group"})
    sparing_df = pd.DataFrame(sparing_df)
    df = y_df.join(sparing_df)

    if save_csv: 
        df.to_csv("file_kmean.csv",index=False)

    return df


if __name__ == "__main__":

    dataset_path = "C:/Users/soont/OneDrive/Desktop/H1/AnnaMatching/Anna-Matching Survey (Responses).csv"
    training_df, sparing_df = preprocessing_csv_to_df(dataset_path)
    training_df.to_csv('preprocessing_file.csv', index = False)
