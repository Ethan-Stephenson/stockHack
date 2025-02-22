import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = yf.download("FUBO", start="2024-06-01", end="2025-02-22")

with open("FUBO.csv", "w") as file:
    data.to_csv("FUBO.csv", index=False)

with open("FUBO.csv", "a") as file:
    file.write("From 2024-06-03 to 2025-01-22")

#print(data.head())
#print(data.describe())
#print(data.shape)

# Visualizing the opening prices of the data.
#plt.figure(figsize=(16,8))
#plt.title('Fubo')
#plt.xlabel('Days')
#plt.ylabel('Opening Price USD ($)')
#plt.plot(data["Close"])
#plt.show()

data2 = data["Close"]
data2 = pd.DataFrame(data2)
shift = 15

data2.to_csv("TEST.csv", index=False)

data2['Prediction'] = data2.shift(-shift)
print(data2.tail())
