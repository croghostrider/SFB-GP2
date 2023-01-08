#!/usr/bin/env python3
import pandas as pd
import streamlit as st


def load_weather():
    st.set_page_config(page_title="Weather", page_icon="📈")
    st.sidebar.header("Weather")

    # Load the weather data
    df = pd.read_csv("src/data/jena_weather_2020.csv")

    # Convert the date column to a datetime object
    df["Date Time"] = pd.to_datetime(df["Date Time"])

    # Create columns
    col1, col2 = st.columns(2)

    with col1:
        # Add a title
        st.title("Weather data for")

    with col2:
        # Use a date picker to allow the user to select a specific date
        selected_date = st.date_input(
            "",
            value=df["Date Time"].min(),
            max_value=df["Date Time"].max(),
            min_value=df["Date Time"].min(),
        )

    # Filter the dataframe to only show data for the selected date
    df_filtered = df[df["Date Time"].dt.date == selected_date]

    # Get the list of columns in the data
    column_names = df_filtered.columns.tolist()

    # Select the columns to use for the line charts
    selected_columns = st.multiselect("Select columns", column_names)

    if selected_columns:
        # Select the columns to use for the line charts
        df_filtered = df_filtered.rename(columns={"Date Time": "index"}).set_index(
            "index"
        )

        # Create tabs
        tab1, tab2 = st.tabs(["one chart", "multiple charts"])

        with tab1:
            # Create a line chart with each selected column
            st.line_chart(df_filtered[selected_columns])

        with tab2:
            # Create a line chart for each selected column
            for column in selected_columns:
                st.line_chart(df_filtered[column])


load_weather()
