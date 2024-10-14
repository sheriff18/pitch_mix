import pandas as pd
import streamlit as st
import plotly.express as px

# Load the predictions data
file_path = "xgboost_predictions_2024.csv"
predictions_df = pd.read_csv(file_path)

# Initialize the Streamlit app
st.set_page_config(page_title="Pitch Mix Predictions by Player for 2024 MLB Season", layout="wide")

# Title of the app
st.title("Pitch Mix Predictions by Player for 2024 MLB Season")

# Dropdown to select player
selected_player = st.selectbox(
    "Select a player:",
    predictions_df['PLAYER_NAME'].unique(),
    index=0
)

# Filter the data for the selected player
player_data = predictions_df[predictions_df['PLAYER_NAME'] == selected_player].iloc[0]

# Create a pie chart for pitch mix
pitch_mix_pie_chart = px.pie(
    names=['Fastball', 'Breaking Ball', 'Off-Speed'],
    values=[player_data['PITCH_TYPE_FB'], player_data['PITCH_TYPE_BB'], player_data['PITCH_TYPE_OS']],
    title=f'Expected Pitch Mix for {selected_player}'
)

# Display the pie chart
st.plotly_chart(pitch_mix_pie_chart, use_container_width=True)

# Create a bar chart for pitch type probabilities
pitch_types = ['Fastball', 'Breaking Ball', 'Off-Speed']
pitch_values = [player_data['PITCH_TYPE_FB'], player_data['PITCH_TYPE_BB'], player_data['PITCH_TYPE_OS']]

pitch_type_bar_chart = px.bar(
    x=pitch_types,
    y=pitch_values,
    title=f'Pitch Type Probabilities for {selected_player}',
    labels={'x': 'Pitch Type', 'y': 'Probability'}
)

# Display the bar chart
st.plotly_chart(pitch_type_bar_chart, use_container_width=True)

# Instructions for deploying the app
st.markdown("### How to Deploy Your App")
st.markdown("1. Install Streamlit if you haven't yet: `pip install streamlit`")
st.markdown("2. Save this script to a `.py` file.")
st.markdown("3. Run your app locally using: `streamlit run your_script_name.py`")
st.markdown("4. To share your app, use Streamlit Cloud to deploy and get a shareable link!")