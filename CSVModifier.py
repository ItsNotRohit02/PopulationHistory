import pandas as pd

# To give corressponding Country Code to Country Names
df = pd.read_csv('PopulationData.csv')
y = df['Country_Name'].factorize()[0]
df.insert(1, column='Country_Code', value=y)
df.to_csv('PopulationData.csv', index=False)

# To display all Country Names and Country Codes in CSV File
df = pd.read_csv('PopulationData.csv')
print(df['Country_Name'].unique())
print(df['Country_Code'].unique())

# To remove unecessary Countries
df = pd.read_csv('PopulationData.csv')
index = df[(df['Country Name'] == 'Timor-Leste') | (df['Country Name'] == 'Solomon Islands') | (
            df['Country Name'] == 'Sao Tome and Principe')
           | (df['Country Name'] == 'Turks and Caicos Islands') | (df['Country Name'] == 'Northern Mariana Islands') | (
                       df['Country Name'] == 'St. Vincent and the Grenadines')].index
df.drop(index, inplace=True)
df.to_csv('PopulationData.csv', index=False)

# To replace Country Names
df = pd.read_csv('PopulationData.csv')
df.Country_Name.replace('Sint Maarten (Dutch part)', 'Sint Maarten', inplace=True)
df.to_csv('PopulationData.csv', index=False)

# To Sort by CountryCode and Year
df = pd.read_csv('Population.csv')
df.sort_values(["Country_Code", "Year"], axis=0, ascending=True, inplace=True, na_position='first')
df.to_csv('Pop.csv', index=True)

# Duplicate Dataframe 12 Times
df = pd.read_csv('Population.csv')
dfcopies = [df] * 12
result = pd.concat(dfcopies)
result.to_csv('Population.csv', index=False)

# Assign Month Values
df = pd.read_csv('Population.csv')
df['Month'] = pd.np.nan
for index, row in df.iterrows():
    df.loc[index, 'Month'] = index % 12 + 1
df.to_csv('Population.csv', index=False)

# Re-assigning matching Population values for each month of each year for each country
df = pd.read_csv('Population.csv')
for cc in range(0, 186):
    if cc == 47:
        continue
    if cc == 59:
        continue
    if cc == 87:
        continue
    for y in range(1960, 2018):
        pop0 = df[(df['Country_Code'] == cc) & (df['Year'] == y) & (df['Month'] == 1)]
        yplus = y + 1
        if y == 2017:
            yplus = y
        pop1 = df[(df['Country_Code'] == cc) & (df['Year'] == yplus) & (df['Month'] == 1)]
        print(pop1, pop0)
        monthchange = int((int(pop1['Population']) - int(pop0['Population'])) / 12)
        print(monthchange)
        for m in range(1, 13):
            newpop = df[(df['Country_Code'] == cc) & (df['Year'] == y) & (df['Month'] == m)]
            df.loc[(df['Country_Code'] == cc) & (df['Year'] == y) & (df['Month'] == m), 'Population'] = \
                int(newpop['Population']) + (monthchange * m)
df.to_csv('Population.csv', index=False)
