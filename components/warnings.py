import streamlit as st
from utils.constants import DISCLAIMER, DATE_WARNING

def show_global_warnings():
    st.warning(DATE_WARNING)
    st.info(DISCLAIMER)
