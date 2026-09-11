import streamlit as st
import pandas as pd
import plotly.express as px

st.title("IPL Data Visualization")

# Load Dataset
df = pd.read_csv("IPL_Matches_Data_2008_2026.csv")

# Calculate Total Runs
df["total_runs"] = (
    df["team1_runs"] +
    df["team2_runs"]
)

# Sidebar Filters
st.sidebar.title("Filters")

selected_season = st.sidebar.selectbox(
    "Select Season",
    sorted(df["season"].dropna().unique())
)

# Filter Dataset
filtered_df = df[
    df["season"] == selected_season
]

# Season Analysis
st.subheader(
    f"Analysis for Season: {selected_season}"
)

# Key Statistics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Matches",
        len(filtered_df)
    )

with col2:
    st.metric(
        "Average Runs",
        round(
            filtered_df["total_runs"].mean(),
            2
        )
    )

with col3:
    st.metric(
        "Highest Score",
        filtered_df["total_runs"].max()
    )

# Team Wins
team_wins = (
    filtered_df["winner"]
    .value_counts()
    .reset_index()
)

team_wins.columns = [
    "Team",
    "Wins"
]

# Winning Teams Bar Chart
fig1 = px.bar(
    team_wins.head(10),
    x="Team",
    y="Wins",
    title="Winning Teams"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# Match Run Distribution
fig2 = px.histogram(
    filtered_df,
    x="total_runs",
    nbins=20,
    title="Match Run Distribution"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)
