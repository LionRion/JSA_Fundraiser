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
    title = st.title("Goal 1: Pie Keegan!")
    goal=75
    my_bar = st.progress(0)
    my_bar.progress(roundedFunds / 75)
elif roundedFunds == 75:
    title = st.title("Goal 1: Pie Keegan: :green[Complete!]")
    goal=75
    my_bar = st.progress(0,)
    my_bar.progress(roundedFunds / 75)
    st.balloons()
elif roundedFunds < 150:
    title = st.title("Goal 2: Pie Sugath!")
    goal=150
    my_bar = st.progress(0)
    my_bar.progress(roundedFunds / 150)
elif roundedFunds == 150:
    title = st.title("Goal 2: Pie Sugath: :green[Complete!]")
    goal=150
    my_bar = st.progress(0)
    my_bar.progress(roundedFunds / 150)
    st.balloons()
elif roundedFunds < 225:
    title = st.title("Goal 3: Pie Soham: :green[Complete!]")
    goal=225
    my_bar = st.progress(0)
    my_bar.progress(roundedFunds / 225)
elif roundedFunds==225:
    title = st.title("Goal 3: Pie Soham: :green[Complete!]")
    goal=225
    my_bar = st.progress(0)
    my_bar.progress(roundedFunds / 225)
    st.balloons()
elif roundedFunds < 300:
    title = st.title("Goal 4: Pie Keegan Again!")
    goal = 300
    my_bar = st.progress(0)
    my_bar.progress(roundedFunds / 300)
else:
    title = st.title("Goal 4: Pie Keegan Again: :green[Complete!]")
    goal = 300
    my_bar = st.progress(0)
    my_bar.progress(1)

percent = roundedFunds/goal * 100

url = "https://www.streamlit.io"

st.divider()

if percent==100 and roundedFunds<300:
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
elif roundedFunds<300:
    dist = 300 - roundedFunds
    st.write("# We are $", dist, " away from our next goal! [Donate now!](%s)" % url)
else:
    dist = 0
    st.write("# We have reached our final goal! [Please donate if you enjoyed!](%s)" % url)

st.divider()

st.write("# We are currently at ", "$", roundedFunds)
st.write("# of our $", goal, " goal!")
#st.write("# That's ", round(percent), "% of the current goal!") # can be removed

