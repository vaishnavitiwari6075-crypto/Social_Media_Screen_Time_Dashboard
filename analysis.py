import streamlit as st
import plotly.express as px
import pandas as pd
df=pd.read_csv("data.csv")
st.sidebar.title("Project Sections")
section = st.sidebar.selectbox(
    " Section",
    [
        "Home",
        "Dashboard",
        "Data Cleaning",
        "Social Media Analysis",
        "Screen Time Analysis",
        "Correlation Analysis",
    ]
)
if section == "Home":
    st.title("Social Media, Screen Time & Mental Health ")
    st.write("This project studies social media usage, screen time",
    "sleep and mental health patterns using data analysis."
    )
    st.write("# Project Objectives")
    st.write("""
    1. To analyze social media usage patterns.
    2. To study daily screen time.
    3. To analyze sleep and lifestyle habits.
    4. To study mental health indicators.
    5. To identify relationships between different factors.
    """)
    st.write("# Dataset")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Participants", len(df))
    col2.metric("Total Variables", len(df.columns))
    col3.metric("Average Screen Time",str(round(df["daily_screen_hours"].mean(), 2)) + " hrs"
    )
elif section =="Dashboard":
    st.title("DASHBOARD")   
    st.sidebar.subheader("Filters")
    gender=st.sidebar.multiselect("Gender",
    df["gender"].unique(),
    default=df["gender"].unique())

    platform=st.sidebar.multiselect("Platform",
    df["most_used_platform"].unique(),
    default=df["most_used_platform"].unique(),
    )
    filtered_df = df[
        (df["gender"].isin(gender)) &
        (df["most_used_platform"].isin(platform))
    ]
    # Metrics
    col1, col2 = st.columns(2)
    col1.metric(
        "Participants",
        len(filtered_df)
    )
    col2.metric(
        "Avg Screen Time",
        str(round(filtered_df["daily_screen_hours"].mean(), 2)) + " hrs"
    )
    st.divider()
    st.subheader("1. Most Used Social Media Platforms")
    platform_count = (
        filtered_df["most_used_platform"]
        .value_counts()
        .reset_index()
    )
    platform_count.columns = ["Platform", "Users"]
    fig1 = px.bar(
        platform_count,
        x="Platform",
        y="Users",
        title="Most Used Social Media Platforms"
    )
    st.plotly_chart(fig1, use_container_width=True)
    st.subheader("2. Daily Screen Time")
    fig2 = px.histogram(
        filtered_df,
        x="daily_screen_hours",
        nbins=15,
        title="Distribution of Daily Screen Time",
        labels={
            "daily_screen_hours": "Daily Screen Time (Hours)"
        }
    )
    st.plotly_chart(fig2, use_container_width=True)
    st.subheader("3. Screen Time and Sleep")
    fig3 = px.scatter(
        filtered_df,
        x="daily_screen_hours",
        y="avg_sleep_hours",
        title="Screen Time vs Sleep",
        labels={
            "daily_screen_hours": "Daily Screen Time (Hours)",
            "avg_sleep_hours": "Average Sleep (Hours)"
        },
        opacity=0.6
    )
    st.plotly_chart(fig3, use_container_width=True)
elif section == "Data Cleaning":
    st.title("Data Cleaning")
    st.write("### Missing Values")
    missing = df.isnull().sum()
    missing_table = pd.DataFrame({
        "Column": missing.index,
        "Missing Values": missing.values
    })
    st.dataframe(
        missing_table,
        use_container_width=True
    )
    st.write(
        "Total missing values:",
        int(df.isnull().sum().sum())
    )
    st.write(
        "Duplicate rows:",
        int(df.duplicated().sum())
    )
    clean_df = df.drop_duplicates()
    st.success(
        "Basic data cleaning has been performed."
    )
    st.write(
        "Rows after removing duplicates:",
        len(clean_df)
    )
elif section == "Social Media Analysis":
    st.title("Social Media Analysis")
    # Graph 1
    platform_data = (
        df["most_used_platform"]
        .value_counts()
        .reset_index()
    )
    platform_data.columns = ["Platform", "Users"]
    st.subheader("Most Used Platforms")
    fig = px.bar(
        platform_data,
        x="Platform",
        y="Users",
        title="Most Used Social Media Platforms"
    )
    st.plotly_chart(fig, use_container_width=True)
    # Graph 2
    st.subheader("Platforms Used by Participants")
    platform_count = (
        df["platforms_used_count"]
        .value_counts()
        .sort_index()
        .reset_index()
    )
    platform_count.columns = [
        "Number of Platforms",
        "Participants"
    ]
    fig2 = px.bar(
        platform_count,
        x="Number of Platforms",
        y="Participants",
        title="Number of Social Media Platforms Used"
    )
    st.plotly_chart(fig2, use_container_width=True)
    # Graph 3
    st.subheader("Main Purpose of Social Media")
    purpose = (
        df["primary_purpose"]
        .value_counts()
        .reset_index()
    )
    purpose.columns = ["Purpose", "Users"]
    fig3 = px.pie(
        purpose,
        names="Purpose",
        values="Users",
        title="Primary Purpose of Social Media"
    )
    st.plotly_chart(fig3, use_container_width=True)
elif section == "Screen Time Analysis":
    st.title("Screen Time Analysis")
    col1, col2, col3 = st.columns(3)
    col1.metric(
        "Average",
        str(round(df["daily_screen_hours"].mean(), 2)) + " hrs"
    )
    col2.metric(
        "Minimum",
        str(round(df["daily_screen_hours"].min(), 2)) + " hrs"
    )
    col3.metric(
        "Maximum",
        str(round(df["daily_screen_hours"].max(), 2)) + " hrs"
    )
    st.subheader("Daily Screen Time Distribution")
    fig = px.histogram(
        df,
        x="daily_screen_hours",
        nbins=20,
        title="Daily Screen Time Distribution"
    )
    st.plotly_chart(fig, use_container_width=True)
    st.subheader("Screen Time vs Sleep")
    fig2 = px.scatter(
        df,
        x="daily_screen_hours",
        y="avg_sleep_hours",
        title="Screen Time vs Average Sleep",
        labels={
            "daily_screen_hours": "Screen Time (Hours)",
            "avg_sleep_hours": "Sleep (Hours)"
        },
        opacity=0.5
    )
    st.plotly_chart(fig2, use_container_width=True)
    st.subheader("Screen Time vs Anxiety")
    fig3 = px.scatter(
        df,
        x="daily_screen_hours",
        y="anxiety_score_0to27",
        title="Screen Time vs Anxiety",
        labels={
            "daily_screen_hours": "Screen Time (Hours)",
            "anxiety_score_0to27": "Anxiety Score"
        },
        opacity=0.5
    )
    st.plotly_chart(fig3, use_container_width=True)
elif section == "Mental Health Analysis":
    st.title("Mental Health Analysis")
    col1, col2, col3 = st.columns(3)
    col1.metric(
        "Average Anxiety",
        round(df["anxiety_score_0to27"].mean(), 2)
    )
    col2.metric(
        "Average Low Mood",
        round(df["low_mood_score_0to27"].mean(), 2)
    )
    col3.metric(
        "Average Loneliness",
        round(df["loneliness_1to10"].mean(), 2)
    )
    st.subheader("Mental Health Scores")
    mental_data = pd.DataFrame({
        "Factor": [
            "Anxiety",
            "Low Mood",
            "Loneliness",
            "FOMO",
            "Social Comparison"
        ],
        "Average Score": [
            df["anxiety_score_0to27"].mean(),
            df["low_mood_score_0to27"].mean(),
            df["loneliness_1to10"].mean(),
            df["fomo_1to10"].mean(),
            df["social_comparison_1to10"].mean()
        ]
    })
    fig = px.bar(
        mental_data,
        x="Factor",
        y="Average Score",
        title="Average Mental Health Related Scores"
    )
    st.plotly_chart(fig, use_container_width=True)
    st.subheader("Wellbeing Band")
    wellbeing = (
        df["wellbeing_band"]
        .value_counts()
        .reset_index()
    )
    wellbeing.columns = ["Wellbeing Band", "Participants"]
    fig2 = px.pie(
        wellbeing,
        names="Wellbeing Band",
        values="Participants",
        title="Wellbeing Distribution"
    )
    st.plotly_chart(fig2, use_container_width=True)
# ---------------- CORRELATION ----------------
elif section == "Correlation Analysis":
    st.title("Correlation Analysis")
    selected_columns = [
        "social_comparison_1to10",
        "physical_activity_days_per_week"
    ]
    correlation = df[selected_columns].corr()
    st.subheader("Correlation Heatmap")
    fig = px.imshow(
        correlation,
        text_auto=".2f",
        aspect="auto",
        title="Correlation Between Social Media, Lifestyle and Mental Health"
    )
    st.plotly_chart(
        fig,
        use_container_width=True
    )
    st.write("### Correlation Table")
    st.dataframe(
        correlation,
        use_container_width=True,
        height=600
    )
   # ---------------- CONCLUSION ----------------
elif section == "Conclusion":
    st.title("Conclusion")
    avg_screen = df["daily_screen_hours"].mean()
    avg_sleep = df["avg_sleep_hours"].mean()
    avg_anxiety = df["anxiety_score_0to27"].mean()
    st.write(
        "Based on the analysis of the dataset, the following "
        "observations can be made:"
    )
    st.write(
        "• Average daily screen time is "
        + str(round(avg_screen, 2))
        + " hours."
    )
    st.write(
        "• Average sleep duration is "
        + str(round(avg_sleep, 2))
        + " hours."
    )
    st.write(
        "• Average anxiety score is "
        + str(round(avg_anxiety, 2))
        + "."
    )
    st.write("""
    The project shows how data analysis can be used to understand
    social media habits, screen time, sleep and mental health
    related patterns.
    The results should be interpreted as patterns in this dataset
    and should not be treated as medical conclusions.
    """)
    st.write("### Future Scope")
    st.write("""
    • A larger dataset can be used.
    • Machine learning can be added for prediction.
    • A recommendation system can be developed.
    • More detailed user behaviour analysis can be performed.
    """) 