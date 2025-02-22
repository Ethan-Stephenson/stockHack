#import finnhub
#import constants

#finnhub_client = finnhub.Client(api_key=f"{constants.FINNHUB_API_KEY}")

import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

data = yf.download("CELH", start="2024-06-01", end="2025-02-22")

with open("CELH.csv", "w") as file:
    data.to_csv("CELH.csv", index=False)

with open("CELH.csv", "a") as file:
    file.write("From 2024-06-03 to 2025-01-22")

print(data.head())
#print(data.info())
#print(data.describe())
#print(data.shape)

# Visualizing the opening prices of the data.
#plt.figure(figsize=(16,8))
#plt.title('Celsuis')
#plt.xlabel('Days')
#plt.ylabel('Opening Price USD ($)')
#plt.plot(data['open'])
#plt.show()

