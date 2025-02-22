import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#### Edit range of data
data = yf.download("FUBO", start="2025-01-01", end="2025-02-22")

data2 = pd.DataFrame(columns=['close'])
data2['close'] = data["Close"]
data2 = pd.DataFrame(data2)

#### Number of days to predict
shift = 3

data2['Prediction'] = data2.shift(-shift)

#CONTENT WARNING: IDK WHAT ANY OF THIS DOES vvvv
X = np.array(data2.drop(columns='Prediction'))[:-shift]
#print(X)

y = np.array(data2['Prediction'])[:-shift]
#print(y)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression

# Implementing Linear and Decision Tree Regression Algorithms.
tree = DecisionTreeRegressor().fit(x_train, y_train)
lr = LinearRegression().fit(x_train, y_train)

x_future = data2.drop(columns='Prediction')[:-shift]
x_future = x_future.tail(shift)
x_future = np.array(x_future)

tree_prediction = tree.predict(x_future)
print(tree_prediction)

lr_prediction = lr.predict(x_future)
print(lr_prediction)

predictions = tree_prediction 
valid = data2[X.shape[0]:]
valid['Predictions'] = predictions

#Something happens
plt.figure(figsize=(16,8))
plt.title("Model")
plt.xlabel('Days')
plt.ylabel('Close Price USD ($)')
plt.plot(data2['close'])
plt.plot(valid[['close', 'Predictions']])
plt.legend(["Original", "Valid", 'Predicted'])
plt.show()