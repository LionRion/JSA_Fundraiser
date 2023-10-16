import streamlit as st
from streamlit_server_state import server_state, server_state_lock, no_rerun
import hmac


def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if hmac.compare_digest(st.session_state["password"], st.secrets["pwd"]):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the password.
        else:
            st.session_state["password_correct"] = False

    # Return True if the passward is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show input for password.
    st.text_input(
        "Password", type="password", on_change=password_entered, key="password"
    )
    if "password_correct" in st.session_state:
        st.error("😕 Password incorrect")
    return False


if not check_password():
    st.stop()  # Do not continue if check_password is not True.

st.set_page_config(page_title="Admin Editor")

st.markdown("# Admin Editor")
st.sidebar.header("Admin Editor")
# st.write(
#    """This demo shows how to use
# [`st.pydeck_chart`](https://docs.streamlit.io/library/api-reference/charts/st.pydeck_chart)
# to display geospatial data."""
# )

if 'num' not in st.session_state:
    st.session_state.num = 0.00
def submit():
    st.session_state.num=float(st.session_state.widget)
    st.session_state.widget=''
    with (server_state_lock["funds"]):
        if "funds" not in server_state:
            server_state.funds = 0.00  # Initial value
        with no_rerun:
            server_state.funds += round(st.session_state.num, 2)
            st.session_state.num = 0.00

st.text_input("Enter a value to increase the slider by:", max_chars=8, key='widget', on_change=submit)



with server_state_lock["funds"]:
    if "funds" not in server_state:
        server_state.funds = 0.00  # Initial value
    with no_rerun:
        server_state.funds = round(st.slider(
            "Shared value", min_value=0.00, max_value=500.00, step=0.01, value=server_state.funds
        ), 2)

st.write(server_state.funds)
