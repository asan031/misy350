import streamlit as st
import json
from pathlib import Path
from datetime import datetime
import uuid
import time

st.set_page_config("Order Application", layout="wide", initial_sidebar_state="expanded")

inventory = [
{"item_id": 1, "name": "Espresso", "unit_price": 2.50, "stock": 40},
{"item_id": 2, "name": "Latte", "unit_price": 4.25, "stock": 25},
{"item_id": 3, "name": "Cold Brew", "unit_price": 3.75, "stock": 30},
{"item_id": 4, "name": "Mocha", "unit_price": 4.50, "stock": 20},
{"item_id": 5, "name": "Blueberry Muffin", "unit_price": 2.95, "stock": 18},
]

if "page" not in st.session_state:
    st.session_state["page"] = "home"

with st.sidebar:
    if st.button("Home",key="home_btn", type="primary", use_container_width=True):
        st.session_state["page"] = "home"
        st.rerun()
    if st.button("Order",key="order_btn", type="primary", use_container_width=True):
        st.session_state["page"] = "order"
        st.rerun()