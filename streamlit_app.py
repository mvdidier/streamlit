import streamlit as st

# Stop execution immediately:
st.stop()
# Rerun script immediately:
st.rerun()
# Navigate to another page:
st.switch_page("pages/my_page.py")

# Define a navigation widget in your entrypoint file
pg = st.navigation(
    st.Page("page1.py", title="Home", url_path="home", default=True)
    st.Page("page2.py", title="Preferences", url_path="settings")
)
pg.run()

# Group multiple widgets:
with st.form(key="my_form"):
    username = st.text_input("Username")
    password = st.text_input("Password")
    st.form_submit_button("Login")

# Define a dialog function
@st.dialog("Welcome!")
def modal_dialog():
    st.write("Hello")

modal_dialog()

# Define a fragment
@st.fragment
def fragment_function():
    df = get_data()
    st.line_chart(df)
    st.button("Update")

fragment_function()
