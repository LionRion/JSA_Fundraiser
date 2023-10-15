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

st.write("# Our funds are currently ", "$", roundedFunds)
st.write("of our goal to ", "$", goal, "!")
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

