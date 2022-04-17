from sklearn.cluster import KMeans
import pandas as pd 
import streamlit as st 


def simple_kmeans(training_df):
    
    std = StandardScaler()
    pca = PCA(n_components=20)
    kmeans = KMeans(n_clusters=4, init='k-means++', n_init=10, max_iter=100, random_state=42)

    
    df_new = std.fit_transform(training_df)
    df_new = pca.fit_transform(df_new)
    identified_clusters = kmeans.fit_predict(df_new)
    # identified_clusters.rename(columns={"0": "group"})

    return identified_clusters


