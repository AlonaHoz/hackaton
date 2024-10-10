
import streamlit as st

value = True
answer_first = False
answer_last = False
answer_name = False
answer_user = False
answer_id = False
answer_password = False
answer_elect = False
answer_water = False
answer_gas = False
answer_fuel = False
existing_account = []
valid_info = []

st.header("Welcome To GREENFOOT🍃")
st.subheader("create your account :)")

First_Name = st.text_input("First name: ")
if len(First_Name) > 0:
    if First_Name.isalpha():
        answer_first = True
        st.text("input valid")
    else:
        st.error("invalid input. please enter letters only")
Last_name = st.text_input("Last name: ")
if len(Last_name) > 0:
    if Last_name.isalpha():
        answer_last = True
        st.text("input valid")
    else:
        st.error("invalid input. please enter letters only")
if  answer_first and answer_last:
    Full_name = First_Name + Last_name
    answer_name = True


ID_Number = st.text_input("ID number: ")
if len(ID_Number) > 0:
    if ID_Number.isdigit():
        answer_id = True
        st.text("input valid")
    else:
        st.error("invalid input. please enter numbers only")

UserName = st.text_input("Username: ")
if len(UserName) > 0:
    if len(UserName) > 3:
        answer_user = True
        st.text("input valid")
    else:
        st.error("invalid input. username must contain at least 4 letters")

Password = st.text_input("Password: ")
if len(Password) > 0:
    if len(Password) > 6:
        answer_password = True
        st.text("input valid")
    else:
        st.error("invalid input. password must be at least 7 letters")



st.subheader("To Get Your FOOTPRINT: ")

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

def existing_acc():
    if answer_name and answer_water and answer_id and answer_elect and answer_fuel and answer_gas\
        and answer_password and answer_user:
        done_state = False
        if not done_state:
            st.text("your account is almost ready! click to finish:")
            done_state = st.button("done")
        if done_state:
            st.text("account successfully created.")
            existing_account.append([UserName, Password])
            return existing_account

def check_payment_valid():
    if answer_elect and answer_water and answer_gas and answer_fuel:
        valid_info.append([answer_elect, answer_water, answer_gas, answer_fuel])
        return valid_info


existing_acc()
check_payment_valid()
