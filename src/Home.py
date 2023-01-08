#!/usr/bin/env python3
import streamlit as st


def main():
    st.set_page_config(
        page_title="Home",
        page_icon="👋",
    )

    # Create the sidebar
    st.sidebar.success("Select a page above.")

    st.markdown(
        """
        # Semester work SFB-GP2

        Hi! this is my first Streamlit app.
        """
    )


if __name__ == "__main__":
    main()
