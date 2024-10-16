
import pandas as pd
from UserDataMangment import *

the_data_base = 'foot_print_data_base.xlsx'
data = pd.read_excel(the_data_base)
df = pd.DataFrame(data, columns=["USERNAME", "WATER_CARBON_FOOT_PRINT"])

df.set_index(['USERNAME', "WATER_CARBON_FOOT_PRINT"])

cfp_local_sum = df["WATER_CARBON_FOOT_PRINT"].sum()

data = pd.read_excel(the_data_base)

print(df)


name = the_list[2]

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
        "FUEL_ACCOUNT_PAYMENT": the_list[7],
        "PERSONAL_CFP_PERCENT": foot_print_list[0],
        "ELECTRICITY_CARBON_FOOT_PRINT": foot_print_list[1],
        "WATER_CARBON_FOOT_PRINT": foot_print_list[2],
        "GAS_CARBON_FOOT_PRINT": foot_print_list[3],
        "FUEL_CARBON_FOOT_PRINT": foot_print_list[4]

    }
    return user_data_dict

def extend_list():
    x = create_user_data_dict()
    cc = pd.concat([data, pd.DataFrame([x])], ignore_index=True)
    return cc

graf = extend_list()


present = pd.DataFrame(data, columns=["USERNAME", "PERSONAL_CFP_PERCENT"])

cfp_local_sum = df["PERSONAL_CFP_PERCENT"].sum()




