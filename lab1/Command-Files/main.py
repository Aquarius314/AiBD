import pandas as pd


df = pd.DataFrame(pd.read_csv("Analysis-Data/converted.csv"))

data = {}

religion_income_rows = pd.DataFrame()

for i, row in df.iterrows():
    income = row['income']
    religion = row['q50']
    new_row = str(income) + "|" + str(religion)
    if not new_row in data.keys():
        data[new_row] = 1
    else:
        data[new_row] = data[new_row] + 1

data_list = []
for key in data.keys():
    data_list.append([key.split("|")[0], key.split("|")[1], data[key]])

data_list.sort()

df2 = pd.DataFrame(data_list, columns=['Income', 'Religion', 'Count'])

for i, row in df2.iterrows():
    print(row.values)

export_csv = df2.to_csv('Analysis-Data/income-and-religion.csv')
