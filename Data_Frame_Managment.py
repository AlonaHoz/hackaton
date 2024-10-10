import pandas as pd


exiting = 'Data (2).xlsx'
data = pd.read_excel(exiting)

df = pd.DataFrame(data, columns=['USERNAME','CARBON_FOOT_PRINT',])

df.set_index(['USERNAME', 'CARBON_FOOT_PRINT'])

cfp_local_sum = df['CARBON_FOOT_PRINT'].sum()

print(df)

exiting = 'Data (2).xlsx'

name =input("name:")
cfp = int(input("cfp:"))

new_data = {'USERNAME': [name], 'CARBON_FOOT_PRINT': [cfp]}

# Load existing workbook
wb = load_workbook(existing_file)

# Select the active sheet
ws = wb.active

# Append new data
for row in new_data:
    ws.append(row)

# Save the workbook
wb.save(existing_file)
print(df)




