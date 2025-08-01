import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    df = pd.read_csv("./data/cleaned_mta_ridership.csv", parse_dates=["date"])
    return df

df = load_data()

st.sidebar.title("Filters")

# get unique years for dropdown
year_options = sorted(df["date"].dt.year.unique())
year = st.sidebar.selectbox("Select Year", year_options)

modes = ["Subway", "Bus", "LIRR", "Metro-North"]
mode_column_map = {
    "Subway": "subways_total_estimated_ridership",
    "Bus": "buses_total_estimated_ridership",
    "LIRR": "lirr_total_estimated_ridership",
    "Metro-North": "metro_north_total_estimated_ridership"
}

mode = st.sidebar.selectbox("Get Estimates by Line", modes)
mode_column = mode_column_map[mode]

df_year = df[df["date"].dt.year == year]

st.title("📊 MTA Ridership Dashboard")
st.markdown(f"### {mode} Ridership in {year}")

# KPI metrics
total_rides = df_year[mode_column].sum()
avg_rides = round(df_year[mode_column].mean(), 2)
peak_day = df_year.loc[df_year[mode_column].idxmax(), "date"].strftime("%Y-%m-%d")

st.metric(label="Total Rides", value=f"{total_rides:,}")
st.metric(label="Average Daily Rides", value=f"{avg_rides:,.0f}")
st.metric(label="Peak Day", value=peak_day)

# line Chart
st.line_chart(df_year.set_index("date")[mode_column])

# raw Data Table
with st.expander("See Raw Data"):
    st.dataframe(df_year[["date", mode_column]].reset_index(drop=True))

# average Ridership by Day of Week
st.markdown("### 📅 Average Ridership by Day of Week")

df_year["day_of_week"] = df_year["date"].dt.day_name()
avg_by_day = df_year.groupby("day_of_week")[mode_column].mean().reindex([
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
])

st.bar_chart(avg_by_day)
