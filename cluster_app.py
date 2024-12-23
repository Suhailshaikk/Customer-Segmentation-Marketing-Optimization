import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

# Load saved models and scaler
kmeans = joblib.load(r"C:\Users\DELL\Desktop\DS_Project\New folder\kmeans_model.pkl")
agg_clustering = joblib.load(r"C:\Users\DELL\Desktop\DS_Project\New folder\agg_clustering.pkl")
dbscan = joblib.load(r"C:\Users\DELL\Desktop\DS_Project\New folder\dbscan_model.pkl")
scaler = joblib.load(r"C:\Users\DELL\Desktop\DS_Project\New folder\scaler.pkl")

# Title of the Streamlit App
st.title("Customer Segmentation Using Multiple Clustering Techniques")
st.write("""
This app allows you to segment customers using **KMeans**, **Agglomerative Clustering**, and **DBSCAN**.  
Upload your dataset and choose a clustering algorithm.
""")

# File Uploader
uploaded_file = st.file_uploader(r"C:\Users\DELL\Desktop\DS_Project\New folder\Mall_Customers set.csv")

if uploaded_file is not None:
    # Load and display the uploaded data
    data = pd.read_csv(uploaded_file)
    st.write("### Uploaded Data")
    st.write(data.head())

    # Feature selection
    features = st.multiselect("Select features for clustering:", data.columns)
    if features:
        X = data[features]

        # Scale the data
        X_scaled = scaler.transform(X)

        # Select clustering algorithm
        algorithm = st.selectbox("Select a Clustering Algorithm:", 
                                 ["KMeans", "Agglomerative Clustering", "DBSCAN"])

        # Perform clustering
        if algorithm == "KMeans":
            clusters = kmeans.predict(X_scaled)
            data['Cluster'] = clusters
            st.write("**KMeans Clustering Applied**")

        elif algorithm == "Agglomerative Clustering":
            clusters = agg_clustering.fit_predict(X_scaled)
            data['Cluster'] = clusters
            st.write("**Agglomerative Clustering Applied**")

        elif algorithm == "DBSCAN":
            clusters = dbscan.fit_predict(X_scaled)
            data['Cluster'] = clusters
            st.write("**DBSCAN Clustering Applied**")

        # Display clustered data
        st.write("### Clustered Data")
        st.write(data.head())

        # Visualization
        st.write("### Cluster Visualization")
        fig, ax = plt.subplots()
        sns.scatterplot(x=X_scaled[:, 0], y=X_scaled[:, 1], hue=data['Cluster'], palette="viridis", s=100)
        plt.title(f"{algorithm} Results")
        plt.xlabel(features[0])
        plt.ylabel(features[1])
        st.pyplot(fig)

        # Download the clustered results
        csv = data.to_csv(index=False).encode('utf-8')
        st.download_button("Download Clustered Data", data=csv, file_name="clustered_results.csv", mime="text/csv")
    else:
        st.warning("Please select at least two features.")
else:
    st.info("Please upload a CSV file to begin.")
