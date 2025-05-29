# HawkeyeParkingInsights 駐車洞察

**HawkeyeParkingInsights** is a project focused on analyzing parking data to generate insights and forecast future parking occupancy. This repository contains the complete end-to-end pipeline, from data loading and exploratory data analysis to model training, prediction, and interactive visualization.

---

## 📜 Project Overview

This project aims to leverage parking data to understand occupancy patterns, identify peak times, and predict future demand. The insights derived can be valuable for parking management, resource allocation, and improving the overall parking experience.

---

## 📂 Directory Structure

Here's a breakdown of the project's directory structure:

* **`data/`**: Contains the raw datasets used for this analysis. This is the starting point for all data processing and modeling.
* **`processed_data/`**: Stores intermediate datasets generated during various experimentation and data preparation phases. These files represent a cleaned or transformed version of the raw data.
* **`reports/`**: Includes generated CSV files and images of interactive dashboards. These are likely outputs from the `interactive_report.ipynb` notebook, providing snapshots of key visualizations and data summaries.
* **`forecasts/`**: Contains the final inferences and results from the forecasting models. This directory holds the outputs of the predictive analysis.
* **`app/`**: This directory houses the Streamlit application.
    * **`app.py`**: A basic Streamlit application designed to visualize the parking predictions.
* **`peak_occupancy_predictions_2025.csv`**: This CSV file contains the final forecasted peak occupancy data for the year 2025.

---

## 📓 Notebooks

This project utilizes Jupyter Notebooks for different stages of the analysis:

* **`forecast.ipynb`**: This is the core notebook detailing the entire end-to-end process. It covers:
    * **Data Loading**: Importing the necessary datasets.
    * **Exploratory Data Analysis (EDA)**: Investigating the data to uncover patterns, anomalies, and insights.
    * **Interactive Dashboards**: (Potentially initial versions or components) Visualizations to understand data characteristics.
    * **Model Training**: Developing and training predictive models for forecasting parking occupancy.
    * **Prediction**: Generating future parking occupancy forecasts.
    This notebook serves as a comprehensive guide to the methodology and implementation.

* **`interactive_report.ipynb`**: This notebook focuses on creating interactive visualizations of the dataset. It's likely used for in-depth exploration and presentation of data trends and patterns. The outputs in the `reports/` directory are generated from this notebook.

---

## 🚀 Getting Started

### Prerequisites

Ensure you have Python installed, along with the necessary libraries. Key libraries likely include:

* pandas
* numpy
* scikit-learn
* matplotlib
* seaborn
* streamlit
* (Potentially others like Prophet, statsmodels, etc., based on the modeling techniques in `forecast.ipynb`)

You can typically install these using pip:
```bash
pip install pandas numpy scikit-learn matplotlib seaborn streamlit