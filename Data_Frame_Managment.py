
import pandas as pd


exiting = 'foot_print_data_base.xlsx'
data = pd.read_excel(exiting)

df = pd.DataFrame(data, columns=["USERNAME", "WATER_CARBON_FOOT_PRINT"])

df.set_index(['USERNAME', "WATER_CARBON_FOOT_PRINT"])

cfp_local_sum = df["WATER_CARBON_FOOT_PRINT"].sum()

exiting = 'foot_print_data_base.xlsx'

name =input("name:")
cfp = int(input("cfp:"))

new_data = {"FULL_NAME": ["MIKEY"],
        "ID_NUMBER": ["id"],
        "USERNAME": ["SAMY"],
        "PASSWORD": ["password"],
        "ELECTRICAL_ACCOUNT_PAYMENT": ["elec_payment"],
        "WATER_ACCOUNT_PAYMENT": ["water_payment"],
        "GAS_ACCOUNT_PAYMENT": ["gas_payment"],
        "FUEL_ACCOUNT_PAYMENT": ["fuel_payment"],
        "PERSONAL_CFP_PERCENT": ["arbon_foot_print"],
        "ELECTRICITY_CARBON_FOOT_PRINT": ["electricity_cfp"],
        "WATER_CARBON_FOOT_PRINT": ["water_cfp"],
        "GAS_CARBON_FOOT_PRINT": ["gas_cfp"],
        "FUEL_CARBON_FOOT_PRINT": [86]}


df_new = pd.DataFrame(new_data)

writer = pd.ExcelWriter('foot_print_data_base.xlsx', mode = 'a', if_sheet_exists= 'overlay')

df_new.to_excel(writer, index=False, header=False, startrow = len(data) +1)

writer.close()

data = pd.read_excel(exiting)

print(df)


