# 🌙 Sleep Time Analysis Dashboard

An interactive web-based dashboard built with **Python, Streamlit, and Pandas** to track sleep patterns, analyze sleep duration, and visualize sleep quality insights.

The application allows users to record their daily sleep schedules, monitor key performance indicators (KPIs), and explore sleep duration trends through an intuitive dashboard.

## 📊 Project Overview

The Sleep Time Analysis Dashboard transforms daily sleep records into meaningful visual insights. It helps users understand their sleeping habits by tracking bedtime, wake-up time, sleep duration, and subjective sleep quality.

The dashboard provides an interactive interface for recording sleep data, reviewing sleep statistics, and exploring sleep quality distribution.

## ✨ Key Features

- **Sleep Tracking:** Record daily bedtime, wake-up time, and sleep quality.
- **Automated Duration Calculation:** Calculate sleep duration in hours, including sleep schedules that cross midnight.
- **Interactive Dashboard:** Display important sleep statistics through KPI cards.
- **Sleep Duration Analysis:** Visualize daily sleep duration trends using bar charts.
- **Sleep Quality Distribution:** Analyze the distribution of Excellent, Good, Fair, and Poor sleep ratings.
- **Weekly Summary:** Review average sleep duration and sleep-related insights.
- **Data Management:** View recorded sleep data in a structured tabular format.
- **CSV Export:** Download sleep records for further analysis.

## 🛠️ Technologies Used

### Programming Language
- Python

### Libraries & Frameworks
- **Streamlit:** Interactive web application and dashboard development.
- **Pandas:** Data manipulation, processing, and analysis.
- **Datetime:** Date and time handling, including sleep duration calculations.

### Data Visualization
- Streamlit Charts
- Interactive bar charts and KPI metrics

## 🖥️ Dashboard Preview

The dashboard includes the following sections:

### 1. Main Analytics Dashboard
Displays average sleep duration, total records, shortest sleep, and longest sleep along with a sleep duration trend chart.

### 2. Sleep Entry Form
Allows users to enter the date, bedtime, wake-up time, and sleep quality through an interactive sidebar form.

### 3. Weekly Breakdown
Provides sleep duration summaries, health guideline comparisons, and sleep quality distribution.

### 4. Raw Sleep Data
Displays recorded sleep information in a structured table with an option to download the data as a CSV file.

## ⚙️ Installation & Setup

### Prerequisites

Make sure the following software is installed on your system:

- Python
- pip (Python package installer)
- Git (optional, for cloning the repository)

### Step 1: Clone the Repository

```bash
git clone https://github.com/sujalteli/Sleep-Time-Analysis-Dashboard.git
```

Navigate to the project directory:

```bash
cd Sleep-Time-Analysis-Dashboard
```

### Step 2: Install Dependencies

Install the required Python libraries:

```bash
pip install -r requirements.txt
```

### Step 3: Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The dashboard will open in your default browser.

If it does not open automatically, visit:

http://localhost:8501

## 📁 Project Structure

```text
Sleep-Time-Analysis-Dashboard/
│
├── app.py
├── requirements.txt
├── README.md
└── Sleep_Time_Analysis_Report.docx
```

## 📈 Key Insights

The dashboard helps users explore:

- Average sleep duration across recorded entries.
- Changes in sleep duration over time.
- Minimum and maximum sleep duration.
- Distribution of sleep quality ratings.
- Whether average sleep duration meets the recommended 7–9 hours of sleep for adults.

## 🔄 Application Workflow

1. Enter daily sleep information using the sidebar form.
2. Automatically calculate sleep duration using Python.
3. Process and organize the data using Pandas.
4. Generate sleep statistics and summary metrics.
5. Visualize sleep patterns through interactive charts.
6. Review the analysis and download the recorded data as CSV.

## 🚀 Future Enhancements

- Monthly and yearly sleep trend analysis.
- Persistent database storage for long-term sleep records.
- Sleep schedule reminder notifications.
- Integration with wearable fitness trackers.
- Advanced sleep pattern analysis and personalized insights.

## 🎯 Learning Outcomes

Through this project, I gained practical experience in:

- Python programming and data processing.
- Building interactive dashboards using Streamlit.
- Data manipulation and analysis with Pandas.
- Creating meaningful data visualizations.
- Developing a functional web-based analytics application.

This project represents another step in my journey toward becoming a Data Analyst and building practical, data-driven applications.

## 👨‍💻 Author

**Sujal Teli**

Aspiring Data Analyst | Python | Data Analytics | Data Visualization

[LinkedIn](https://www.linkedin.com/in/sujal-teli/) | [GitHub](https://github.com/sujalteli)

---

⭐ If you find this project interesting, feel free to explore the repository and share your feedback!
