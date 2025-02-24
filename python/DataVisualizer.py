import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#### Edit range of data
#data = yf.download("CELH", start="2025-01-01", end="2025-02-24")
#data = yf.download("CVNA", start="2025-02-01", end="2025-02-24")
#data = yf.download("UPST", start="2025-01-01", end="2025-02-24")
#data = yf.download("ALT", start="2025-01-01", end="2025-02-24")
data = yf.download("FUBO", start="2025-01-01", end="2025-02-24")




data2 = pd.DataFrame(columns=['close', 'yestClose', 'volume'])
data2['close'] = data["Close"]
data2['volume'] = data['Volume']
data2['yestClose'] = data2['close'].shift(1)
data2 = pd.DataFrame(data2)

#### Number of days to predict
shift = 3

data2['Prediction'] = data2['close'].shift(-shift)
#print(data2)

# X: our training variables
X = np.array(data2.drop(columns='Prediction'))[:-shift]

# Y: our stored predictions
y = np.array(data2['Prediction'])[:-shift]

# We have yet to use x_test or y_test. Ignore for now. 
#from sklearn.model_selection import train_test_split
#x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.5)

from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
# Implementing Decision Tree Regression Algorithms.
tree = DecisionTreeRegressor().fit(X, y)

x_future = data2.drop(columns='Prediction')[:]
x_future = x_future.tail(shift)
x_future = pd.DataFrame(x_future)
#print(x_future)

#predicts data based on the values we pass to the future
tree_prediction = tree.predict(x_future)
#print(tree_prediction)

prediction2 = tree_prediction
valid = data2[X.shape[0]:]
#print(X.shape[0])
valid['Prediction'] = prediction2
#print(valid)

# Create a date range for the future
future_dates = pd.date_range("2025-02-24", "2025-02-26")

# Assuming valid['Prediction'] has the same number of entries as future_dates
future = pd.DataFrame({'Date': future_dates, 'Prediction': valid['Prediction'].values[:len(future_dates)]})

# Set 'Date' as the index
future.set_index('Date', inplace=True)

historical_data = data2['close']

print(historical_data)
print(future)

#Something happens
plt.figure(figsize=(16,8))
plt.title("Model")
plt.xlabel('Days')
plt.ylabel('Close Price USD ($)')

# Extract the last historical data point
last_date = historical_data.index[-1]
last_price = historical_data.iloc[-1]

# Extract the first future prediction
first_future_date = future.index[0]
first_future_price = future.iloc[0]['Prediction']

# Plot a connecting line
plt.plot([last_date, first_future_date], [last_price, first_future_price], color='green', linestyle='dashed', label="Connecting Line")


# Update legend to include the new line
plt.legend(["Original", "Tree Prediction", "Connecting Line"])


# Plot historical data in one color
plt.plot(historical_data.index, historical_data, color='blue')

# Plot future predictions in another color, ensuring continuity
plt.plot(future.index, future, color='red')

# Add legend to distinguish between the two

plt.show()

