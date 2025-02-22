import finnhub
import constants
import pandas as pd


finnhub_client = finnhub.Client(api_key=f"{constants.FINNHUB_API_KEY}")

res = finnhub_client.company_news('CELH', _from="2022-06-01", to="2024-06-10")




print(pd.DataFrame(res))

