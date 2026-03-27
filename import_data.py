import pandas as pd
from sqlalchemy import create_engine

# Connect to PostgreSQL
engine = create_engine('postgresql://postgres:1234@localhost:5432/health_project1')

# ---- Import health_spend ----
df1 = pd.read_csv(r"C:\Users\kavya\OneDrive\Desktop\projects\health_project\data\health_expen_all_countries.csv.csv", skiprows=4)
df1 = df1[['Country Name', 'Country Code'] + [str(y) for y in range(2000, 2022)]]
df1 = df1.melt(id_vars=['Country Name', 'Country Code'], var_name='year', value_name='health_expenditure')
df1.columns = ['country_name', 'country_code', 'year', 'health_expenditure']
df1 = df1.dropna(subset=['health_expenditure'])
df1['year'] = df1['year'].astype(int)
df1['health_expenditure'] = pd.to_numeric(df1['health_expenditure'], errors='coerce')
df1 = df1.dropna()
df1.to_sql('health_spend', engine, if_exists='replace', index=False)
print("health_spend imported successfully!")
print("Rows imported:", len(df1))

# ---- Import life_expectancy ----
df2 = pd.read_csv(r"C:\Users\kavya\OneDrive\Desktop\projects\health_project\data\life_expentancy.csv.csv" , skiprows=4)
df2 = df2[['Country Name', 'Country Code'] + [str(y) for y in range(2000, 2022)]]
df2 = df2.melt(id_vars=['Country Name', 'Country Code'], var_name='year', value_name='life_exp')
df2.columns = ['country_name', 'country_code', 'year', 'life_exp']
df2 = df2.dropna(subset=['life_exp'])
df2['year'] = df2['year'].astype(int)
df2['life_exp'] = pd.to_numeric(df2['life_exp'], errors='coerce')
df2 = df2.dropna()
df2.to_sql('life_expectancy', engine, if_exists='replace', index=False)
print("life_expectancy imported successfully!")
print("Rows imported:", len(df2))

# ---- Import infant_mortality ----
df3 = pd.read_csv(r"C:\Users\kavya\OneDrive\Desktop\projects\health_project\data\infant_mortality.csv.csv", skiprows=4)
df3 = df3[['Country Name', 'Country Code'] + [str(y) for y in range(2000, 2022)]]
df3 = df3.melt(id_vars=['Country Name', 'Country Code'], var_name='year', value_name='mortality_rate')
df3.columns = ['country_name', 'country_code', 'year', 'mortality_rate']
df3 = df3.dropna(subset=['mortality_rate'])
df3['year'] = df3['year'].astype(int)
df3['mortality_rate'] = pd.to_numeric(df3['mortality_rate'], errors='coerce')
df3 = df3.dropna()
df3.to_sql('infant_mortality', engine, if_exists='replace', index=False)
print("infant_mortality imported successfully!")
print("Rows imported:", len(df3))

print("✅ ALL 3 TABLES IMPORTED SUCCESSFULLY!")
print(df1.shape)
print(df1.head())
print("after cleaning:", df1.shape)
