import pandas as pd

df = pd.read_csv('/Users/dully/PycharmProjects/life_expectancy_gdp_project/data/all_data.csv')
df = df.rename(columns = {'Life expectancy at birth (years)': 'life_expectancy'})

print(df)