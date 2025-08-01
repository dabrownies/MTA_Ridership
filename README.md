# 🗽 MTA Ridership Dashboard

This project analyzes and visualizes NYC MTA ridership data from 2020–2025.  
It includes a Python-based ETL pipeline and an interactive Streamlit dashboard that helps explore ridership trends across different transit modes.

## What It Does

- Cleans and transforms raw ridership CSV data from the [MTA Open Data Portal](https://data.ny.gov/Transportation/MTA-Daily-Ridership-Data-2020-2025/vxuj-8kew/about_data)
- Outputs a cleaned CSV used to power visualizations
- Interactive dashboard lets users:
  - Filter by year and transit mode (Subway, Bus, LIRR, Metro-North)
  - View total, average, and peak day ridership
  - Explore trends over time and by day of week

## 📊 Live Dashboard

[Launch Streamlit App](https://mtaridership.streamlit.app/)

## Tech Stack

- Python
- pandas
- Streamlit
- Public NYC Open Data

## Setup

```bash
pip install -r requirements.txt
streamlit run streamlit_app/app.py
