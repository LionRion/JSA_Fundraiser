import streamlit as st
import time
import numpy as np
from streamlit_server_state import server_state

st.set_page_config(page_title="Fundraiser Tracker", layout='wide')

st.markdown("# Fundraiser Tracker")
st.sidebar.header("Fundraiser Tracker")

roundedFunds = round(server_state.funds, 2)
goal=0

if roundedFunds < 500:
    goal=500
    my_bar = st.progress(0, text="Goal 1: Dye Keegan's and Shardul's hair!")
    my_bar.progress(roundedFunds / 500, text="Goal 1: Dye Keegan's and Shardul's hair!")
elif roundedFunds == 500:
    goal=500
    my_bar = st.progress(0, text="Goal 1: Dye Keegan's and Shardul's hair!")
    my_bar.progress(roundedFunds / 75, text="Goal 1: Dye Keegan's and Shardul's hair!")
    st.balloons()
elif roundedFunds < 750:
    goal=750
    my_bar = st.progress(0, text="Goal 2: Dye Sugath's and Amrit's hair!")
    my_bar.progress(roundedFunds / 750, text="Goal 2: Dye Sugath's and Amrit's hair!")
elif roundedFunds == 750:
    goal=750
    my_bar = st.progress(0, text="Goal 2: Dye Sugath's and Amrit's hair!")
    my_bar.progress(roundedFunds / 750, text="Goal 2: Dye Sugath's and Amrit's hair!")
    st.balloons()
elif roundedFunds < 1000:
    goal=1000
    my_bar = st.progress(0, text="Goal 3: Dye Soham's and Jeff's hair!")
    my_bar.progress(roundedFunds / 225, text="Goal 3: Dye Soham's and Jeff's hair!")
elif roundedFunds == 1000:
    goal=1000
    my_bar = st.progress(0, text="Goal 3: Dye Soham's and Jeff's hair!")
    my_bar.progress(roundedFunds / 1000, text="Goal 3: Dye Soham's and Jeff's hair!")
    st.balloons()

st.divider()

st.write("# Our funds are currently $", roundedFunds, " out of our goal of $", goal, "!")
percent = roundedFunds/goal * 100
st.write("# That's ", round(percent), "% of the current goal!")

st.divider()

url = "https://www.streamlit.io"

if percent==100 and roundedFunds<1000:
    dist=0
    st.write("# We have :green[completed] the current goal! [Donate now to reveal the next goal!](%s)" % url)
elif roundedFunds<500:
    dist = 75-roundedFunds
    st.write("# We are $", dist, " away from our next goal! [Donate now!](%s)" % url)
elif roundedFunds<750:
    dist = 150 - roundedFunds
    st.write("# We are $", dist, " away from our next goal! [Donate now!](%s)" % url)
elif roundedFunds<1000:
    dist = 225 - roundedFunds
    st.write("# We are $", dist, " away from our next goal! [Donate now!](%s)" % url)
else:
    dist = 0
    st.write("# We have reached our final goal! [Please donate if you enjoyed!](%s)" % url)

