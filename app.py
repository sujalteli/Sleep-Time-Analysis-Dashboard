from datetime import datetime, time, timedelta
import pandas as pd
import streamlit as st  # type: ignore[import-not-found]

# Page Configuration
st.set_page_config(
    page_title="Sleep Time Analysis Dashboard", page_icon="😴", layout="wide"
)

# Initialize Session State with Sample Raw Data
if "sleep_data" not in st.session_state:
  st.session_state.sleep_data = [
      {
          "Date": "2026-06-01",
          "Bedtime": "23:30",
          "Wake Time": "07:15",
          "Quality": "Good",
      },
      {
          "Date": "2026-06-02",
          "Bedtime": "00:00",
          "Wake Time": "06:45",
          "Quality": "Fair",
      },
      {
          "Date": "2026-06-03",
          "Bedtime": "22:45",
          "Wake Time": "06:30",
          "Quality": "Excellent",
      },
      {
          "Date": "2026-06-04",
          "Bedtime": "23:15",
          "Wake Time": "07:00",
          "Quality": "Good",
      },
      {
          "Date": "2026-06-05",
          "Bedtime": "01:00",
          "Wake Time": "08:30",
          "Quality": "Poor",
      },
      {
          "Date": "2026-06-06",
          "Bedtime": "23:00",
          "Wake Time": "07:30",
          "Quality": "Good",
      },
      {
          "Date": "2026-06-07",
          "Bedtime": "22:30",
          "Wake Time": "07:00",
          "Quality": "Excellent",
      },
  ]


# Helper function to calculate duration in hours
def calculate_duration(bedtime_str, waketime_str):
  fmt = "%H:%M"
  t1 = datetime.strptime(bedtime_str, fmt)
  t2 = datetime.strptime(waketime_str, fmt)

  # If wake time is earlier than bedtime, it crossed midnight
  if t2 <= t1:
    t2 += timedelta(days=1)

  duration_seconds = (t2 - t1).total_seconds()
  return round(duration_seconds / 3600, 2)


# Process Data for Dashboard
df = pd.DataFrame(st.session_state.sleep_data)
df["Duration (hrs)"] = df.apply(
    lambda row: calculate_duration(row["Bedtime"], row["Wake Time"]), axis=1
)
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

# --- App Layout ---
st.title("😴 Sleep Time Analysis Dashboard")
st.markdown(
    "Track your sleeping and waking times, analyze sleep duration patterns,"
    " and review weekly averages."
)

# Sidebar: Record New Sleep Entry
st.sidebar.header("📝 Record Sleep Entry")
with st.sidebar.form("sleep_form"):
  entry_date = st.date_input("Date", value=datetime.today())
  bed_time = st.time_input("Bedtime", value=time(23, 0))
  wake_time = st.time_input("Wake Time", value=time(7, 0))
  quality = st.selectbox(
      "Sleep Quality", ["Excellent", "Good", "Fair", "Poor"]
  )

  submitted = st.form_submit_button("Add Entry")
  if submitted:
    new_entry = {
        "Date": entry_date.strftime("%Y-%m-%d"),
        "Bedtime": bed_time.strftime("%H:%M"),
        "Wake Time": wake_time.strftime("%H:%M"),
        "Quality": quality,
    }
    st.session_state.sleep_data.append(new_entry)
    st.success("Sleep record added successfully!")
    st.rerun()

# --- Main Dashboard Metrics ---
avg_sleep = df["Duration (hrs)"].mean()
total_records = len(df)
min_sleep = df["Duration (hrs)"].min()
max_sleep = df["Duration (hrs)"].max()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Average Sleep", f"{avg_sleep:.2f} hrs")
col2.metric("Total Records", f"{total_records} days")
col3.metric("Shortest Sleep", f"{min_sleep:.2f} hrs")
col4.metric("Longest Sleep", f"{max_sleep:.2f} hrs")

st.markdown("---")

# --- Visualizations ---
st.subheader("📊 Sleep Duration Trend")
# Format date for cleaner chart x-axis
chart_df = df.copy()
chart_df["Formatted Date"] = chart_df["Date"].dt.strftime("%b %d")
chart_data = chart_df.set_index("Formatted Date")[["Duration (hrs)"]]

st.bar_chart(chart_data)

# Target line reference note
st.caption(
    "💡 Tip: The recommended healthy sleep range for adults is typically 7 to 9"
    " hours per night."
)

st.markdown("---")

# --- Raw Data and Weekly Analysis ---
tab1, tab2 = st.tabs(["📋 Raw Sleep Data", "📈 Weekly Breakdown"])

with tab1:
  st.subheader("Raw Dataset Log")
  st.dataframe(
      df[["Date", "Bedtime", "Wake Time", "Duration (hrs)", "Quality"]].style.format({
          "Date": lambda x: x.strftime("%Y-%m-%d")
      }),
      use_container_width=True,
  )

  # Download raw data as CSV
  csv = df.to_csv(index=False).encode("utf-8")
  st.download_button(
      label="Download Raw Data as CSV",
      data=csv,
      file_name="sleep_analysis_data.csv",
      mime="text/csv",
  )

with tab2:
  st.subheader("Weekly Summary & Insights")
  # Group by week or show weekly averages
  weekly_avg = avg_sleep
  st.markdown(f"**Weekly Average Sleep Duration:** `{weekly_avg:.2f} hours/night`")

  if weekly_avg >= 7:
    st.success(
        "🎉 Great job! Your average sleep duration meets the optimal health"
        " guidelines."
    )
  else:
    st.warning(
        "⚠️ Your average sleep duration is below 7 hours. Consider adjusting"
        " your bedtime earlier."
    )

  st.markdown("### Quality Distribution")
  quality_counts = df["Quality"].value_counts()
  st.bar_chart(quality_counts)