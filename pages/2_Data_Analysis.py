import streamlit as st
import pandas as pd

st.title("IPL Data Analysis")

# Load Dataset
df = pd.read_csv(r"D:\ETA\IPL_Streamlit_Project\IPL_Matches_Data_2008_2026.csv")

# Calculate Total Runs
df["total_runs"] = (
    df["team1_runs"] +
    df["team2_runs"]
)

# Key Statistics
st.subheader("Key Statistics")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Matches",
    len(df)
)

col2.metric(
    "Seasons",
    df["season"].nunique()
)

col3.metric(
    "Venues",
    df["venue"].nunique()
)

col4.metric(
    "Average Runs",
    round(df["total_runs"].mean(), 2)
)

# Filters
st.subheader("Filters")

selected_season = st.selectbox(
    "Select Season",
    sorted(df["season"].dropna().unique())
)

# Filter Dataset
filtered_df = df[
    df["season"] == selected_season
]

# Display Filtered Data
st.subheader("Filtered Data")

st.dataframe(
    filtered_df,
    use_container_width=True
)