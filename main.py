from clustering import simple_kmeans
from data_preprocessing import preprocessing_csv_to_df,join_id_clts_and_sparing_df


dataset_path = "C:/Users/soont/OneDrive/Desktop/H1/AnnaMatching/Anna-Matching Survey (Responses).csv"


if __name__ == "__main__": 

    training_df, sparing_df = preprocessing_csv_to_df(dataset_path)
    identified_clusters = simple_kmeans(training_df)
    df = join_id_clts_and_sparing_df(identified_clusters,sparing_df,save_csv=False)

    print(df)