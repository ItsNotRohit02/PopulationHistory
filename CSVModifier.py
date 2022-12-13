import pandas as pd

#To give corressponding Country Code to Country Names
df = pd.read_csv('PopulationData.csv')
y = df['Country_Name'].factorize()[0]
df.insert(1,column='Country_Code',value=y)
df.to_csv('PopulationData.csv',index=False)

#To display all Country Names and Country Codes in CSV File
df=pd.read_csv('PopulationData.csv')
print(df['Country_Name'].unique())
print(df['Country_Code'].unique())

#To remove unecessary Countries
df = pd.read_csv('PopulationData.csv')
index = df[(df['Country Name'] == 'Timor-Leste') | (df['Country Name'] == 'Solomon Islands') | (df['Country Name'] == 'Sao Tome and Principe')
           | (df['Country Name'] == 'Turks and Caicos Islands') | (df['Country Name'] == 'Northern Mariana Islands' ) | (df['Country Name'] == 'St. Vincent and the Grenadines')].index
df.drop(index , inplace=True)
df.to_csv('PopulationData.csv',index=False)

#To replace Country Names
df=pd.read_csv('PopulationData.csv')
df.Country_Name.replace('Sint Maarten (Dutch part)', 'Sint Maarten', inplace=True)
df.to_csv('PopulationData.csv',index=False)