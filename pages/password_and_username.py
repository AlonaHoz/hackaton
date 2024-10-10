import streamlit

streamlit.header("GreenFoot🍃")
streamlit.subheader("log into your account :)")
user_name = str(streamlit.text_input("Username: "))
password = str(streamlit.text_input("Password: "))
