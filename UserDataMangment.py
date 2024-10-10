from Main import user_data_list
import consts
from pages import create_new_account


def create_user_data_dict(user_data_list):
    name = get_full_name()
    id = get_id()
    username = get_user_name()
    password = get_password()
    profile_img_file = get_profile_pic_file()
    elec_payment = get_electricity_account_payment()
    water_payment = get_water_account_payment()
    gas_payment = get_gas_account_payment()
    fuel_payment = get_fuel_account_payment()
    carbon_foot_print = calc_carbon_foot_print(elec_payment, water_payment, gas_payment, fuel_payment)
    electricity_cfp = calc_specific_cfp(elec_payment, consts.EMISSION_FACTOR_ELECTRICITY)
    water_cfp = calc_specific_cfp(water_payment, consts.EMISSION_FACTOR_WATER)
    gas_cfp = calc_specific_cfp(gas_payment, consts.EMISSION_FACTOR_GAS)
    fuel_cfp = calc_specific_cfp(fuel_payment, consts.EMISSION_FACTOR_FUEL)
    user_data_dict = {
        "FULL_NAME": create_new_account.Full_Name,
        "ID_NUMBER": create_new_account.ID_Number,
        "USERNAME": create_new_account.UserName,
        "PASSWORD": create_new_account.Password,
        "PROFILE_IMAGE_FILE": None,
        "ELECTRICAL_ACCOUNT_PAYMENT": create_new_account.electrical_payment,
        "WATER_ACCOUNT_PAYMENT": create_new_account.water_payment,
        "GAS_ACCOUNT_PAYMENT": create_new_account.gas_payment,
        "CAR_FUEL_PAYMENT": create_new_account.car_fuel_payment,
        "TOTAL_CARBON_FOOT_PRINT": carbon_foot_print,
        "ELECTRICITY_CARBON_FOOT_PRINT": electricity_cfp,
        "WATER_CARBON_FOOT_PRINT": water_cfp,
        "GAS_CARBON_FOOT_PRINT": gas_cfp,
        "FUEL_CARBON_FOOT_PRINT": fuel_cfp

    }
    user_data_list.append(user_data_dict)
    return user_data_list


def get_full_name():
    full_name = 0
    while not full_name.isalpha():
        full_name = input("enter full name: ")
        if not full_name.isalpha():
            print("invalid input")
        full_name = [full_name]
    return full_name


def get_id():
    id_num = 0
    while (not len(id_num) == 9) or (not id_num.is_integer()):
        id_num = input("enter your id number: ")
        if (not len(id_num) == 9) or (not id_num.is_integer()):
            print("invalid input")
    id_num = [id_num]
    return id_num


def get_user_name():
    user_name = input("enter user name: ")
    valid_username = True
    if len(user_data_list) > 1:
        for user_data_dict in user_data_list:
            if user_data_dict["USER_NAME"] != user_name:
                valid_username = False
    while not valid_username:
        user_name = input("enter user name: ")
    user_name = [user_name]
    return user_name


def get_password():
    password = input("enter password")
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
    return carbon_foot_print


def calc_specific_cfp(source, emission):
    cfp = source * emission
    return cfp
