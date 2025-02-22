import yfinance as yf

#Celsuis
data = yf.download("CELH", start="2024-06-01", end="2025-02-22") #edit range
data.to_csv("CELH.csv", index=False)
with open("CELH.csv", "a") as file:
    file.write("From 2024-06-03 to 2025-01-22") #edit last line of file 

data = yf.download("CVNA", start="2024-06-01", end="2025-02-22")
data.to_csv("CVNA.csv", index=False)
with open("CVNA.csv", "a") as file:
    file.write("From 2024-06-03 to 2025-01-22")

data = yf.download("UPST", start="2024-06-01", end="2025-02-22")
data.to_csv("UPST.csv", index=False)
with open("UPST.csv", "a") as file:
    file.write("From 2024-06-03 to 2025-01-22")

data = yf.download("ALT", start="2024-06-01", end="2025-02-22")
data.to_csv("ALT.csv", index=False)
with open("ALT.csv", "a") as file:
    file.write("From 2024-06-03 to 2025-01-22")

data = yf.download("FUBO", start="2024-06-01", end="2025-02-22")
data.to_csv("FUBO.csv", index=False)
with open("FUBO.csv", "a") as file:
    file.write("From 2024-06-03 to 2025-01-22")
