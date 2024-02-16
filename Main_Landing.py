import streamlit as st
import streamlit.components.v1 as components
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


if roundedFunds < 500:
    title = st.title("Goal 1: Dye Keegan's and Shardul's hair!")
    goal=500
    my_bar = st.progress(0)
    my_bar.progress(roundedFunds / 500)
elif roundedFunds == 500:
    title = st.title("Goal 1: Dye Keegan's and Shardul's hair: :green[Complete!]")
    goal=500
    my_bar = st.progress(0,)
    my_bar.progress(roundedFunds / 75)
    st.balloons()
elif roundedFunds < 750:
    title = st.title("Goal 2: Dye Sugath's and Amrit's hair!")
    goal=750
    my_bar = st.progress(0)
    my_bar.progress(roundedFunds / 750)
elif roundedFunds == 750:
    title = st.title("Goal 2: Dye Sugath's and Amrit's hair: :green[Complete!]")
    goal=750
    my_bar = st.progress(0)
    my_bar.progress(roundedFunds / 750)
    st.balloons()
elif roundedFunds < 1000:
    title = st.title("Goal 3: Dye Soham's and Jeff's hair!")
    goal = 1000
    my_bar = st.progress(0)
    my_bar.progress(roundedFunds / 1000)
else:
    title = st.title("Goal 3: Dye Soham's and Jeff's hair: :green[Complete!]")
    goal = 1000
    my_bar = st.progress(0)
    my_bar.progress(1)

percent = roundedFunds/goal * 100

url = "https://fundraise.jsa.org/give/517274/#!/donation/checkout"

#components.iframe(url) #for when I can figure out how to get JSA website to accept new ports


st.divider()

if percent==100 and roundedFunds<1000:
    dist=0
    st.write("# We have :green[completed] the current goal! [Donate now to reveal the next goal!](%s)" % url)
elif roundedFunds<500:
    dist = round(500-roundedFunds, 2)
    st.write("# We are $", dist, " away from our next goal! [Donate now!](%s)" % url)
elif roundedFunds<750:
    dist = round(750 - roundedFunds, 2)
    st.write("# We are $", dist, " away from our next goal! [Donate now!](%s)" % url)
elif roundedFunds<1000:
    dist = round(1000 - roundedFunds, 2)
    st.write("# We are $", dist, " away from our next goal! [Donate now!](%s)" % url)
else:
    dist = 0
    st.write("# We have reached our final goal! [Please donate if you enjoyed!](%s)" % url)

st.divider()

st.write("# We are currently at ", "$", roundedFunds)
st.write("# of our $", goal, " goal!")
#st.write("# That's ", round(percent), "% of the current goal!") # can be removed

