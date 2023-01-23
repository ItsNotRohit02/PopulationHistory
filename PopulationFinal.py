import pandas as pd
from sklearn.tree import DecisionTreeRegressor
import joblib

rawdata = pd.read_csv("PopulationData.csv")
X = rawdata.drop(columns=['Country_Name', 'Population'])
y = rawdata['Population']

model = DecisionTreeRegressor()
model.fit(X, y)

joblib.dump(model, 'PopulationMLModel.joblib')
