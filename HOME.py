import streamlit as st
import time

st.write("Welcome to IPL Web App Project")

# Define a dialog function
@st.dialog("Welcome!")
def modal_dialog():
    st.write("Hello")

# modal_dialog()

# Define a fragment
@st.fragment
def fragment_function():
    st.write("Click the button below")
    st.button("Update")

fragment_function()

# st.balloons()
# st.snow()
# st.toast("Warming up...")
# st.error("Error message")
# st.warning("Warning message")
# st.info("Info message")
# st.success("Success message")
# # st.exception(e)

# with st.spinner(text="In progress"):
#     time.sleep(1)
#     st.success("Done")

# Show and update progress bar
# bar = st.progress(0)
# for i in range(0,100):
#     time.sleep(0.1)
#     bar.progress(i)

# with st.status("Authenticating...") as s:
#     time.sleep(1)
#     st.write("Some long response.")
#     s.update(label="Response")


with st.form(key="my_form"):
    username = st.text_input("Username")
    password = st.text_input("Password")
    st.form_submit_button("Login")

data = [1,2,3,4]
st.data_editor(data)

# st.download_button("Download file", data)

if st.toggle("Enable"):
    st.write("Enabled!")

"_This_ is some **Markdown***"

st.date_input("Your birthday")
st.time_input("Meeting time")

st.slider("Pick a number", 0, 100)
st.select_slider("Pick a size", ["S", "M", "L"])
st.code("for i in range(8): foo()")
