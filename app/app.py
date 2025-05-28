import streamlit as st
import pandas as pd
from datetime import date, datetime

# --- CONFIG ---
CSV_PATH = 'peak_occupancy_predictions_2025.csv'
START_DATE = date(2025, 5, 1)
END_DATE   = date(2025, 12, 31)

# --- DATA LOADING ---
@st.cache_data
def load_predictions(path):
    try:
        df = pd.read_csv(path)
    except FileNotFoundError:
        st.error(f"❗ Could not find CSV at `{path}`. Check your path and try again.")
        return pd.DataFrame()
    except Exception as e:
        st.error(f"❗ Error loading CSV: {e}")
        return pd.DataFrame()

    # normalize column names
    df.columns = df.columns.str.strip()
    if 'date' in df.columns:
        df.rename(columns={'date': 'Date'}, inplace=True)
    if 'predicted_peak_occupancy' in df.columns:
        df.rename(columns={'predicted_peak_occupancy': 'PredictedPeakOccupancy'}, inplace=True)

    # parse dates
    df['Date'] = pd.to_datetime(df['Date']).dt.date
    return df

# --- APP LAYOUT ---
st.set_page_config(page_title="🅿️ Hawkeye Parking Predictor", layout="wide")
st.title("Peak Parking Lot Usage Forecasts")

predictions_df = load_predictions(CSV_PATH)
if predictions_df.empty:
    st.stop()  # abort if no data

# Controls
col1, col2 = st.columns(2)
with col1:
    selected_date = st.date_input(
        "📅 Select a date",
        value=START_DATE,
        min_value=START_DATE,
        max_value=END_DATE
    )
with col2:
    available_lots = sorted(predictions_df['LotNumber'].unique().tolist())
    selected_lot = st.selectbox("🚗 Select a parking lot", available_lots)

# Action
if st.button("Get Prediction"):
    # 1) Show the single prediction
    mask = (
        (predictions_df['Date'] == selected_date) &
        (predictions_df['LotNumber'] == selected_lot)
    )
    sel = predictions_df.loc[mask]
    if sel.empty:
        st.warning(f"No forecast found for lot {selected_lot} on {selected_date}.")
    else:
        val = int(round(sel['PredictedPeakOccupancy'].iloc[0]))
        st.metric(
            label=f"Predicted Peak for Lot {selected_lot} on {selected_date}",
            value=f"{val} vehicles"
        )

    # 2) Show full date table, with the chosen lot highlighted
    daily = predictions_df[predictions_df['Date'] == selected_date].copy()
    daily['PredictedPeakOccupancy'] = daily['PredictedPeakOccupancy'].round().astype(int)

    def highlight_row(row):
        # if this is the selected lot, highlight all columns
        if row['LotNumber'] == selected_lot:
            return ['background-color: yellow'] * len(row)
        return [''] * len(row)

    styled = daily.style.apply(highlight_row, axis=1)
    st.write("### All lots on that date")
    st.dataframe(styled)

# Sidebar
st.sidebar.header("About")
st.sidebar.info(
    "This app uses a forecasting model to predict daily peak occupancy for each parking lot.\n\n"
    "Choose any date or lot above to see the forecast."
)
st.sidebar.markdown("---")
st.sidebar.markdown("Powered by HawkeyeParkingInsights Team")
