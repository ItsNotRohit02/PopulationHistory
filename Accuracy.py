import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

rawdata=pd.read_csv("PopulationData.csv")
X=rawdata.drop(columns=['Country_Name','Population'])
y=rawdata['Population']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)


model=DecisionTreeRegressor()
model.fit(X_train,y_train)
p=model.predict(X_test)

accuracy = r2_score(y_test,p)
print('The accuracy of the ML Model is ',accuracy)
