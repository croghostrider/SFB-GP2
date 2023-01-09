#!/usr/bin/env python3
from pathlib import Path

import streamlit as st


def main():
    st.set_page_config(
        page_title="Home",
        page_icon="👋",
    )

    # Create the sidebar
    st.sidebar.success("Select a page above.")

    # Read the README.md file and show the contents
    intro_markdown = read_markdown_file("README.md")
    st.markdown(intro_markdown, unsafe_allow_html=True)


def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()


if __name__ == "__main__":
    main()
