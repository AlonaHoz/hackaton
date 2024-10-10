import streamlit as st


st.header("GreenFoot🍃")
st.subheader("log into your account :)")
user_name = str(st.text_input("Username: "))
password = str(st.text_input("Password: "))

def check_for_user(user, pw, existing):
    answer_elect = False
    answer_water = False
    answer_gas = False
    answer_fuel = False

    if user in existing and pw in existing:
        st.subheader("login successful! Get Your FOOTPRINT: ")

    electrical_payment = st.text_input("Electrical payment: ")
    if len(electrical_payment) > 0:
        if electrical_payment.isdigit():
            answer_elect = True
            st.text("input valid")
        else:
            st.error("invalid input.")

    water_payment = st.text_input("Water payment: ")
    if len(water_payment) > 0:
        if water_payment.isdigit():
            answer_water = True
            st.text("input valid")
        else:
            st.error("invalid input.")

    gas_payment = st.text_input("Gas payment: ")
    if len(gas_payment) > 0:
        if gas_payment.isdigit():
            answer_gas = True
            st.text("input valid")
        else:
            st.error("invalid input.")

    car_fuel_payment = st.text_input("Car Fuel payment: ")
    if len(car_fuel_payment) > 0:
        if car_fuel_payment.isdigit():
            answer_fuel = True
            st.text("input valid")
        else:
            st.error("invalid input.")

    if answer_elect and answer_gas and answer_fuel and answer_water:
        st.text("perfect! :) data updated")

