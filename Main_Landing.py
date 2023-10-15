import streamlit as st
from streamlit_server_state import server_state, server_state_lock

st.set_page_config(
    page_title="Fundraiser Counter!",
    layout='wide',
    initial_sidebar_state="collapsed"
)

with server_state_lock["funds"]:  # Lock the "count" state for thread-safety
    if "funds" not in server_state:
        server_state.funds = 0.00

server_state.funds = server_state.funds

st.markdown("""
    <style>
        section[data-testid="stSidebar"][aria-expanded="true"]{
            display: none;
        }
    </style>
    """, unsafe_allow_html=True)

roundedFunds = round(server_state.funds,2)

if roundedFunds<75:
    dist = 75-roundedFunds
elif roundedFunds<150:
    dist = 150 - roundedFunds
elif roundedFunds<225:
    dist = 225 - roundedFunds
else:
    dist = 0

st.write("# We are $", dist, " away from our next goal! Donate now!")
st.write("*link*")
