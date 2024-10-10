import streamlit as st
value = True

st.header("Welcome To GREENFOOT:")

st.subheader("Enter your:  ")

Full_Name = st.text_input("Full Name: ")
UserName = st.text_input("UserName: ")
ID_Number = st.text_input("ID_Number: ")
Password = st.text_input("Password: ")

st.subheader("To Get Your FOOTPRINT: ")

electrical_payment = st.text_input("Electrical payment: ")
water_payment = st.text_input("Water payment: ")
gas_payment = st.text_input("Gas payment: ")
car_fuel_payment = st.text_input("Car Fuel payment: ")