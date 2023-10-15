import streamlit as st
import time
import numpy as np
from streamlit_server_state import server_state

st.set_page_config(page_title="Fundraiser Tracker", layout='wide')

st.markdown("# Fundraiser Tracker")
st.sidebar.header("Fundraiser Tracker")

roundedFunds = round(server_state.funds, 2)
goal=0

if roundedFunds < 75:
    goal=75
    my_bar = st.progress(0, text="Goal 1: Pie Sugath!")
    my_bar.progress(roundedFunds / 75, text="Goal 1: Pie Sugath!")
elif roundedFunds == 75:
    goal=75
    my_bar = st.progress(0, text="Goal 1: Pie Sugath!")
    my_bar.progress(roundedFunds / 75, text="Goal 1: Pie Sugath!")
    st.balloons()
elif roundedFunds < 150:
    goal=150
    my_bar = st.progress(0, text="Goal 2: Pie Keegan!")
    my_bar.progress(roundedFunds / 150, text="Goal 2: Pie Keegan!")
elif roundedFunds == 150:
    goal=150
    my_bar = st.progress(0, text="Goal 1: Pie Keegan!")
    my_bar.progress(roundedFunds / 150, text="Goal 2: Pie Keegan!")
    st.balloons()
elif roundedFunds < 225:
    goal=225
    my_bar = st.progress(0, text="Goal 3: Pie Soham!")
    my_bar.progress(roundedFunds / 225, text="Goal 3: Pie Soham!")
else:
    goal=225
    my_bar = st.progress(0, text="Goal 1: Pie Soham!")
    my_bar.progress(roundedFunds / 225, text="Goal 3: Pie Soham!")
    st.balloons()

st.divider()

st.write("# Our funds are currently $", roundedFunds, " out of our goal of $", goal, "!")
percent = roundedFunds/goal * 100
st.write("# That's ", round(percent), "% of the current goal!")

st.divider()

url = "https://www.streamlit.io"

if percent==100 and roundedFunds<225:
    dist=0
    st.write("# We have :green[completed] the current goal! [Donate now to reveal the next goal!](%s)" % url)
elif roundedFunds<75:
    dist = 75-roundedFunds
    st.write("# We are $", dist, " away from our next goal! [Donate now!](%s)" % url)
elif roundedFunds<150:
    dist = 150 - roundedFunds
    st.write("# We are $", dist, " away from our next goal! [Donate now!](%s)" % url)
elif roundedFunds<225:
    dist = 225 - roundedFunds
    st.write("# We are $", dist, " away from our next goal! [Donate now!](%s)" % url)
else:
    dist = 0
    st.write("# We have reached our final goal! [Please donate if you enjoyed!](%s)" % url)

