#!/usr/bin/env python3
import redis
import streamlit as st
from streamlit_autorefresh import st_autorefresh


def load_automation():
    st.set_page_config(page_title="Automation", page_icon="💡")
    st.sidebar.header("Automation")

    st_autorefresh(interval=2000, key="dataframerefresh")

    # Connect to Redis server
    r = redis.Redis(**st.secrets.db_credentials)

    # Add a title to the app
    st.title("Light and Heating Control")

    # Add a header and description
    st.header("Control your lights, ventilation and heating from anywhere!")
    st.markdown(
        "Use this app to turn your lights on and off and adjust the temperature in your home."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        _load_automation("Living room", r)
    with col2:
        _load_automation("Bedroom", r)
    with col3:
        _load_automation("Bathroom", r)


# crate columns contents
def _load_automation(room, r):
    st.header(room)

    st.subheader("Temperature")
    # Add a slider for adjusting the temperature
    temperature = st.slider(
        label="Set the temperature (°C)",
        min_value=15,
        max_value=26,
        value=_get_values(room, "temperature", r),
        key=room + "Temperature",
    )

    st.subheader("Ventilation")
    # Add a radio-button for adjusting the ventilation
    ventilation = st.radio(
        label="Set the level",
        options=("1", "2", "3"),
        index=_get_values(room, "ventilation", r)-1,
        horizontal=True,
        key=room + "ventilation",
    )

    st.subheader("Light")
    # Add a slider for adjusting the brightness of the lights
    brightness = st.slider(
        label="Set the brightness",
        min_value=0,
        max_value=100,
        value=_get_values(room, "light", r),
        key=room + "brightness",
    )

    if brightness > 0:
        # Add a button for turning the selected lights off
        if st.button(label="off", key=room + "off"):
            brightness = 0
    # Add a button for turning the selected lights on
    elif st.button(label="on", key=room + "on"):
        brightness = 100

    # Save the values
    _save_values(room, "temperature", temperature, r)
    _save_values(room, "ventilation", ventilation, r)
    _save_values(room, "light", brightness, r)


def _get_values(room, type, r):
    return int(r.get(room + type), 10)


def _save_values(room, type, value, r):
    r.set(room + type, value)


load_automation()
