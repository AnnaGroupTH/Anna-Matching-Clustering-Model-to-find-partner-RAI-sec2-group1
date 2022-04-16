from sklearn.cluster import KMeans
import pandas as pd 
import streamlit as st 


def simple_kmeans(training_df):
    
    kmeans = KMeans(n_clusters=8)
    identified_clusters = kmeans.fit_predict(training_df)
    # identified_clusters.rename(columns={"0": "group"})

    return identified_clusters


