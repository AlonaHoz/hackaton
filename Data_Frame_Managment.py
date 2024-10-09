import pandas as pd


data = pd.read_excel(r"Data.xlsx")

df = pd.DataFrame(data, columns=['USERNAME','CARBON_FOOT_PRINT'])

df.set_index(['USERNAME', 'CARBON_FOOT_PRINT'])

print(df.to_string(index=False))
