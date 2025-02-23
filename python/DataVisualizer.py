import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#### Edit range of data
data = yf.download("ALT", start="2024-01-01", end="2025-02-22")

data2 = pd.DataFrame(columns=['close', 'yestClose', 'volume'])
data2['close'] = data["Close"]
data2['volume'] = data["Volume"]
data2 = pd.DataFrame(data2)

#### Number of days to predict
shift = 3

data2['yestClose'] = data2['close'].shift(1)
data2['Prediction'] = data2['close'].shift(-shift)

print(data2)

# X: our training variables
X = np.array(data2.drop(columns='Prediction'))[:-shift]

# Y: our stored predictions
y = np.array(data2['Prediction'])[:-shift]

# We have yet to use x_test or y_test. Ignore for now. 
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.5)

from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
# Implementing Decision Tree Regression Algorithms.
tree = DecisionTreeRegressor().fit(x_train, y_train)

x_future = data2.drop(columns='Prediction')[:-shift]
x_future = x_future.tail(shift)
x_future = np.array(x_future)
print(x_future)

tree_prediction = tree.predict(x_future)
print(tree_prediction)

prediction2 = tree_prediction
valid = data2[X.shape[0]:]
valid['Prediction2'] = prediction2

#Something happens
plt.figure(figsize=(16,8))
plt.title("Model")
plt.xlabel('Days')
plt.ylabel('Close Price USD ($)')
plt.plot(data2['close'])
plt.plot(valid[['close', 'Prediction2']])
plt.legend(["Original", "Valid", "Tree Prediction"])
plt.show()

