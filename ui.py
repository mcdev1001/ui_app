import streamlit as st
import pandas as pd



def main():
    # Set page title
    st.title("Anomaly Detection for Infrastructure Monitoring")
    st.subheader("Sponsor: Bank of America")
    st.text("Mentors:\nJoji Thomas\nSurina Puri\nChan Simpson\nChris Delao\nTeam:\nZac Ching\nDanielle Joan Mapili\nDevon McDermott\nFaculty Advisor:\nHongsheng Zhou")
    
    st.header("Objective")
    st.text("Proactively identify issues related to network infrastructure\nthat may lead to disruption of services and operations")

    # First header with subtext
    
    st.header("Dataset Introduction")
    st.subheader("How we Built our Data")
    st.text("To begin our synthtic dataset we expanded upon a small data sample using \na log generator. We generated additional features including date/time and server \nname to mimic a real log one might find at BOA. \nWe completed our working dataset by injecting synthetic anamolies.")

    # Second header with subtext
    st.header("Log Data View")
    st.text("Our working dataset with injected anomalies")

    # Specify the path to your CSV file
    csv_file_path = "injected dataset - injected dataset.csv"

    # Read CSV file
    df = pd.read_csv(csv_file_path)

    # Display the dataset
    st.dataframe(df)

    # Scatter chart for the 'DATE' feature
    st.header("Scatter Plot ")
    st.subheader("Visualization of the data\nin terms of event summary and date/time")

    # Check if the 'DATE' column exists in the dataset
    if 'DATE' in df.columns:
        # Convert the 'DATE' column to datetime if it's not already
        df['DATE'] = pd.to_datetime(df['DATE'])

        # Create a scatter chart
        st.scatter_chart(data=df, x='DATE', y='SUMMARY')  # Replace 'Your_Target_Column' with the actual column name you want to plot
    else:
        st.warning("The 'DATE' column does not exist in the dataset.")


    
    # Third header with subtext
    st.header("Model Training")
    st.subheader("We will employ 2-3 algorithms for in house use for detection of anomalous behavior.")
    st.text("Algorithms to test:\nLogBert\nLogAnomaly\nDeepLog\nLogCluster\niForest")
    st.header("More Updates to Come Soon!")
    st.text("We will be working on our design over break! Happy Holidays!")
if __name__ == "__main__":
    main()
