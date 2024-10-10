from Main import user_data_list
import consts
import streamlit
from pages import password_and_username
from pages import create_new_account


def collect_data():
    name = get_full_name(create_new_account.Full_Name)
    id = get_id(create_new_account.ID_Number)
    username = get_user_name(create_new_account.UserName)
    password = get_password(create_new_account.Password)
    elec_payment = get_electricity_account_payment()
    water_payment = get_water_account_payment()
    gas_payment = get_gas_account_payment()
    fuel_payment = get_fuel_account_payment()
    the_list = [name, id, username, password, elec_payment, water_payment, gas_payment,
                fuel_payment]
    return the_list

the_list = collect_data()

def calc_list():
    carbon_foot_print = calc_carbon_foot_print(the_list[4], the_list[5], the_list[6], the_list[7])
    electricity_cfp = calc_specific_cfp(the_list[4], consts.EMISSION_FACTOR_ELECTRICITY)
    water_cfp = calc_specific_cfp(the_list[5], consts.EMISSION_FACTOR_WATER)
    gas_cfp = calc_specific_cfp(the_list[6], consts.EMISSION_FACTOR_GAS)
    fuel_cfp = calc_specific_cfp(the_list[7], consts.EMISSION_FACTOR_FUEL)
    list_list = [carbon_foot_print, electricity_cfp, water_cfp, gas_cfp, fuel_cfp]
    return list_list

foot_print_list = calc_list()

def create_user_data_dict():
    user_data_dict = {
        "FULL_NAME": the_list[0],
        "ID_NUMBER": the_list[1],
        "USERNAME": the_list[2],
        "PASSWORD": the_list[3],
        "ELECTRICAL_ACCOUNT_PAYMENT": the_list[4],
        "WATER_ACCOUNT_PAYMENT": the_list[5],
        "GAS_ACCOUNT_PAYMENT": the_list[6],
        "CAR_FUEL_PAYMENT": the_list[7],
        "TOTAL_CARBON_FOOT_PRINT": foot_print_list[0],
        "ELECTRICITY_CARBON_FOOT_PRINT": foot_print_list[1],
        "WATER_CARBON_FOOT_PRINT": foot_print_list[2],
        "GAS_CARBON_FOOT_PRINT": foot_print_list[3],
        "FUEL_CARBON_FOOT_PRINT": foot_print_list[4]

    }
    user_data_list.append(user_data_dict)
    return user_data_list


def add_percent_to_user_data(user_data_list, username, cfp_local_sum):
    for user in user_data_list:
        if user["USERNAME"] == username:
            username_elec_perc = calc_personal_user_percent_of_local_cfp_sum(cfp_local_sum,
                                                                             user["ELECTRICITY_CARBON_FOOT_PRINT"])
            username_water_perc = calc_personal_user_percent_of_local_cfp_sum(cfp_local_sum,
                                                                              user["WATER_CARBON_FOOT_PRINT"])
            username_gas_perc = calc_personal_user_percent_of_local_cfp_sum(cfp_local_sum,
                                                                            user["GAS_CARBON_FOOT_PRINT"])
            username_fuel_perc = calc_personal_user_percent_of_local_cfp_sum(cfp_local_sum,
                                                                             user["FUEL_CARBON_FOOT_PRINT"])
            user["USER_ELEC_PERCENT"] = username_elec_perc
            user["USER_ WATER_PERCENT"] = username_water_perc
            user["USER_GAS_PERCENT"] = username_gas_perc
            user["USER_FUEL_PERCENT"] = username_fuel_perc
            return user


def get_user_data_dict(user_data_list, username):
    for user_dict in user_data_list:
        if user_dict["USERNAME"] == username:
            return user_dict


def get_full_name(full_name):
    while not full_name.isalpha():
        if not full_name.isalpha():
            streamlit.text("invalid input")
        full_name = [full_name]
    return full_name


def get_id(ID_number):
    while (not len(ID_number) == 9) or (not ID_number.is_integer()):
        if (not len(ID_number) == 9) or (not ID_number.is_integer()):
            streamlit.text("invalid input")
    id_num = [ID_number]
    return ID_number


def get_user_name(user_name):
    valid_username = True
    if len(user_data_list) > 1:
        for user_data_dict in user_data_list:
            if user_data_dict["USER_NAME"] != user_name:
                valid_username = False
    while not valid_username:
        user_name = [user_name]
    return user_name


def get_password(password):
    password = [password]
    return password


def get_profile_pic_file():
    pass


def get_electricity_account_payment():
    elec_payment = 0
    while not elec_payment.is_integer():
        elec_payment = input("enter your electricity_account_payment: ")
        if not elec_payment.is_integer():
            print("invalid input")
    elec_payment = [elec_payment]
    return elec_payment


def get_water_account_payment():
    water_payment = 0
    while not water_payment.is_integer():
        water_payment = input("enter your electricity_account_payment: ")
        if not water_payment.is_integer():
            print("invalid input")
    water_payment = [water_payment]
    return water_payment


def get_gas_account_payment():
    gas_payment = 0
    while not gas_payment.is_integer():
        gas_payment = input("enter your electricity_account_payment: ")
        if not gas_payment.is_integer():
            print("invalid input")
    gas_payment = [gas_payment]
    return gas_payment


def get_fuel_account_payment():
    fuel_payment = 0
    while not fuel_payment.is_integer():
        fuel_payment = input("enter your electricity_account_payment: ")
        if not fuel_payment.is_integer():
            print("invalid input")
    fuel_payment = [fuel_payment]
    return fuel_payment


def calc_carbon_foot_print(elec_payment, water_payment, gas_payment, fuel_payment):
    carbon_foot_print = (elec_payment * consts.EMISSION_FACTOR_ELECTRICITY +
                         water_payment * consts.EMISSION_FACTOR_WATER +
                         gas_payment * consts.EMISSION_FACTOR_GAS +
                         fuel_payment * consts.EMISSION_FACTOR_FUEL)
    return [carbon_foot_print]


def calc_specific_cfp(source, emission):
    cfp = source * emission
    return [cfp]


def calc_personal_user_percent_of_local_cfp_sum(cfp_local_sum, user_cfp_sum):
    user_percent = (user_cfp_sum * 100) / cfp_local_sum
    return [user_percent]


def calc_specific_cfp(source, emission):
    cfp = source * emission
    return cfp
