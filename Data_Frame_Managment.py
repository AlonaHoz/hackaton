import pandas as pd


data = pd.read_excel(r"Data (2).xlsx")

df = pd.DataFrame(data, columns=['USERNAME','CARBON_FOOT_PRINT',])

df.set_index(['USERNAME', 'CARBON_FOOT_PRINT'])

c = 'CARBON_FOOT_PRINT'

b = df[c].sum()

print(df)
