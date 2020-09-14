#Author: Asad Qadri
# ML Handling Categorical Feature - Python Project 2

# Importing essential libraries:
import pandas as pd

#Importing Dataset:
df = pd.read_csv("Startup_Profit.csv")

#Creating Dummy Variables:
df1 = pd.get_dummies(df['State'], drop_first = True)

#Concatinating df1 and df:
df = pd.concat([df1, df], axis = 1)

#Drop State Column:
df.drop('State', axis = 1, inplace = True)

#Convering Into Dependent and Independent Feature:
X = df.iloc[:,:-1]
y = df.iloc[:,[5]]

#Train Test Split:
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.25)      #25%

#Applying Linear Regression Model:
from sklearn.linear_model import LinearRegression
regression = LinearRegression()
regression.fit(X_train, y_train)

#Prdiction:
y_pred = regression.predict(X_test)

#Need to Check R Square Value to see Accuracy Level:
from sklearn.metrics import r2_score
accuracy_score = r2_score(y_test, y_pred)
print(accuracy_score)