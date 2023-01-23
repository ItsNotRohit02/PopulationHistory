import joblib
import pandas as pd
import streamlit as st

model = joblib.load('PopulationMLModel.joblib')
st.set_page_config(page_title="Population History", page_icon=":family:")
st.title('Welcome to Population History!')

with st.container():
    st.header('How we display Population History ?')
    st.write('We use a Machine Learning Algorithm called Decision Tree Regression to learn from data'
             ' collected over 55 years for 188 countries to create a complex and accurate model to display the population of selected'
             ' country.')

with st.container():
    st.write('---')
    st.header('Select from Options below')
    country = st.selectbox('Select the Country (Start Typing to Search)',
                           ['India', 'United States', 'China', 'Pakistan',
                            'United Kingdom', 'Afghanistan', 'Angola', 'Albania', 'Andorra', 'United Arab Emirates',
                            'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Burundi',
                            'Belgium', 'Bangladesh', 'Bulgaria', 'Bahrain', 'Bahamas', 'Belarus', 'Bermuda',
                            'Bolivia', 'Brazil', 'Barbados', 'Bhutan', 'Botswana', 'Canada', 'Switzerland',
                            'Channel Islands', 'Chile', 'Cameroon', 'Congo', 'Colombia', 'Comoros',
                            'Costa Rica', 'Caribbean', 'Cuba', 'Curacao', 'Cayman Islands', 'Cyprus',
                            'Czech Republic', 'Germany', 'Djibouti', 'Dominica', 'Denmark',
                            'Dominican Republic', 'Algeria', 'Ecuador', 'Egypt', 'Eritrea', 'Spain',
                            'Estonia', 'Ethiopia', 'Finland', 'Fiji', 'France', 'Gabon',
                            'Georgia', 'Ghana', 'Gibraltar', 'Guinea', 'Gambia', 'Greece', 'Grenada',
                            'Greenland', 'Guatemala', 'Guam', 'Hong Kong', 'Honduras', 'Croatia', 'Haiti',
                            'Hungary', 'Indonesia', 'Isle of Man', 'Ireland',
                            'Iran, Islamic Rep.', 'Iraq', 'Iceland', 'Israel', 'Italy', 'Jamaica', 'Jordan',
                            'Japan', 'Kazakhstan', 'Kenya', 'Cambodia', 'South Korea', 'Kuwait', 'Lebanon',
                            'Liberia', 'Libya', 'St. Lucia', 'Liechtenstein', 'Sri Lanka', 'Lesotho',
                            'Lithuania', 'Luxembourg', 'Latvia', 'Macao', 'St. Martin', 'Morocco', 'Monaco',
                            'Madagascar', 'Maldives', 'Mexico', 'Marshall Islands', 'North Macedonia',
                            'Mali', 'Malta', 'Myanmar', 'Montenegro', 'Mongolia', 'Mozambique',
                            'Mauritania', 'Mauritius', 'Malawi', 'Malaysia', 'Namibia', 'New Caledonia',
                            'Niger', 'Nigeria', 'Nicaragua', 'Netherlands', 'Norway', 'Nepal', 'Nauru',
                            'New Zealand', 'Oman', 'Panama', 'Peru', 'Philippines', 'Palau',
                            'Papua New Guinea', 'Poland', 'Puerto Rico', 'Portugal', 'Paraguay',
                            'French Polynesia', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saudi Arabia',
                            'Sudan', 'Senegal', 'Singapore', 'Sierra Leone', 'El Salvador', 'San Marino',
                            'Somalia', 'South Sudan', 'Suriname', 'Slovak Republic', 'Slovenia', 'Sweden',
                            'Eswatini', 'Seychelles', 'Syria', 'Chad', 'Togo', 'Thailand', 'Tajikistan',
                            'Turkmenistan', 'Tonga', 'Trinidad', 'Tunisia', 'Turkey', 'Tuvalu', 'Tanzania',
                            'Uganda', 'Ukraine', 'Uruguay', 'Uzbekistan', 'Venezuela',
                            'British Virgin Islands', 'Virgin Islands (U.S.)', 'Vietnam', 'Vanuatu',
                            'Samoa', 'Kosovo', 'Yemen', 'South Africa', 'Zambia', 'Zimbabwe', 'Gaza',
                            'Serbia', 'Sint Maarten'])
    countrydict = {'Afghanistan': 0, 'Angola': 1, 'Albania': 2, 'Andorra': 3, 'United Arab Emirates': 4,
                   'Argentina': 5, 'Armenia': 6, 'Australia': 7, 'Austria': 8, 'Azerbaijan': 9, 'Burundi': 10,
                   'Belgium': 11, 'Bangladesh': 12, 'Bulgaria': 13, 'Bahrain': 14, 'Bahamas': 15, 'Belarus': 16,
                   'Bermuda': 17,
                   'Bolivia': 18, 'Brazil': 19, 'Barbados': 20, 'Bhutan': 21, 'Botswana': 22, 'Canada': 23,
                   'Switzerland': 24,
                   'Channel Islands': 25, 'Chile': 26, 'China': 27, 'Cameroon': 28, 'Congo': 29, 'Colombia': 30,
                   'Comoros': 31,
                   'Costa Rica': 32, 'Caribbean': 33, 'Cuba': 34, 'Curacao': 35, 'Cayman Islands': 36, 'Cyprus': 37,
                   'Czech Republic': 38, 'Germany': 39, 'Djibouti': 40, 'Dominica': 41, 'Denmark': 42,
                   'Dominican Republic': 43, 'Algeria': 44, 'Ecuador': 45, 'Egypt': 46, 'Eritrea': 47, 'Spain': 48,
                   'Estonia': 49, 'Ethiopia': 50, 'Finland': 51, 'Fiji': 52, 'France': 53, 'Gabon': 54,
                   'United Kingdom': 55,
                   'Georgia': 56, 'Ghana': 57, 'Gibraltar': 58, 'Guinea': 59, 'Gambia': 60, 'Greece': 61, 'Grenada': 62,
                   'Greenland': 63, 'Guatemala': 64, 'Guam': 65, 'Hong Kong': 66, 'Honduras': 67, 'Croatia': 68,
                   'Haiti': 69,
                   'Hungary': 70, 'Indonesia': 71, 'Isle of Man': 72, 'India': 73, 'Ireland': 74,
                   'Iran, Islamic Rep.': 75, 'Iraq': 76, 'Iceland': 77, 'Israel': 78, 'Italy': 79, 'Jamaica': 80,
                   'Jordan': 81,
                   'Japan': 82, 'Kazakhstan': 83, 'Kenya': 84, 'Cambodia': 85, 'South Korea': 86, 'Kuwait': 87,
                   'Lebanon': 88,
                   'Liberia': 89, 'Libya': 90, 'St. Lucia': 91, 'Liechtenstein': 92, 'Sri Lanka': 93, 'Lesotho': 94,
                   'Lithuania': 95, 'Luxembourg': 96, 'Latvia': 97, 'Macao': 98, 'St. Martin': 99, 'Morocco': 100,
                   'Monaco': 101,
                   'Madagascar': 102, 'Maldives': 103, 'Mexico': 104, 'Marshall Islands': 105, 'North Macedonia': 106,
                   'Mali': 107, 'Malta': 108, 'Myanmar': 109, 'Montenegro': 110, 'Mongolia': 111, 'Mozambique': 112,
                   'Mauritania': 113, 'Mauritius': 114, 'Malawi': 115, 'Malaysia': 116, 'Namibia': 117,
                   'New Caledonia': 118,
                   'Niger': 119, 'Nigeria': 120, 'Nicaragua': 121, 'Netherlands': 122, 'Norway': 123, 'Nepal': 124,
                   'Nauru': 125,
                   'New Zealand': 126, 'Oman': 127, 'Pakistan': 128, 'Panama': 129, 'Peru': 130, 'Philippines': 131,
                   'Palau': 132,
                   'Papua New Guinea': 133, 'Poland': 134, 'Puerto Rico': 135, 'Portugal': 136, 'Paraguay': 137,
                   'French Polynesia': 138, 'Qatar': 139, 'Romania': 140, 'Russia': 141, 'Rwanda': 142,
                   'Saudi Arabia': 143,
                   'Sudan': 144, 'Senegal': 145, 'Singapore': 146, 'Sierra Leone': 147, 'El Salvador': 148,
                   'San Marino': 149,
                   'Somalia': 150, 'South Sudan': 151, 'Suriname': 152, 'Slovak Republic': 153, 'Slovenia': 154,
                   'Sweden': 155,
                   'Eswatini': 156, 'Seychelles': 157, 'Syria': 158, 'Chad': 159, 'Togo': 160, 'Thailand': 161,
                   'Tajikistan': 162,
                   'Turkmenistan': 163, 'Tonga': 164, 'Trinidad': 165, 'Tunisia': 166, 'Turkey': 167, 'Tuvalu': 168,
                   'Tanzania': 169,
                   'Uganda': 170, 'Ukraine': 171, 'Uruguay': 172, 'United States': 173, 'Uzbekistan': 174,
                   'Venezuela': 175,
                   'British Virgin Islands': 176, 'Virgin Islands (U.S.)': 177, 'Vietnam': 178, 'Vanuatu': 179,
                   'Samoa': 180, 'Kosovo': 181, 'Yemen': 182, 'South Africa': 183, 'Zambia': 184, 'Zimbabwe': 185,
                   'Gaza': 186,
                   'Serbia': 187, 'Sint Maarten': 188}
    c = countrydict[country]
    y = int(st.slider('Select Year', 1960, 2017, value=2000))

with st.container():
    p = model.predict([[y, c]])
    pop = int(p[0])
    st.metric(label='Population', value=f"{pop:,d}")

with st.container():
    st.write("---")
    st.header('Graphical Representation of Population')
    rawdata = pd.read_csv("PopulationData.csv")
    country = rawdata[rawdata['Country_Code'] == c]
    st.line_chart(data=country, x='Year', y='Population')

with st.container():
    st.caption("Made by Rohit")
    st.markdown("[![Foo](https://cdn-icons-png.flaticon.com/24/25/25231.png)](https://github.com/ItsNotRohit02)")
