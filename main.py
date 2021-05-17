import requests
import pandas as pd
import json
import numpy as np
import apikey
from twilio.rest import Client
import math

pd.options.mode.chained_assignment = None

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


def request_builder_alpha_vantage(function, symbol, key):
    # return f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&interval={interval}&apikey={apikey}
    request = f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&apikey={key}'
    return request


def request_builder_news(date, topic, key):
    request = f'https://newsapi.org/v2/everything?q={topic}&from={date}&to={date}&sortBy=popularity&apiKey={key}'
    return request


# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

response = requests.get(request_builder_alpha_vantage("TIME_SERIES_DAILY", STOCK, apikey.APIKEY_ALFAVANTAGE))

df = pd.DataFrame(json.loads(response.content)['Time Series (Daily)'])
count_a_vals = df.T["1. open"].values
count_a_vals = np.array(count_a_vals)
count_a_vals = count_a_vals.astype(np.float32)

count_b_vals = df.T["4. close"].values
count_b_vals = np.array(count_b_vals)
count_b_vals = count_b_vals.astype(np.float32)

df = df.T
df['diff'] = 0
df['diff'].iloc[:-1] = (count_a_vals[:-1] - count_b_vals[1:]) / count_b_vals[:-1] * 100
df = df[df['diff'] > 2]

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
response = requests.get(request_builder_news(df.axes[0].values[0], "TESLA", apikey.APIKEY_NEWS))

data = json.loads(response.content)
df2 = pd.json_normalize(data['articles'])
print(df2[2:5]['title'].values)

# STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.


client = Client(apikey.account_sid, apikey.auth_token)

message = client.messages.create(
    from_='whatsapp:+14155238886',
    body=f'''Tesla up {math.floor(df['diff'].values[0])}%, Headline: {str(df2[2:3]['title'].values[0])}''',
    to='whatsapp:+420737445008'
)

print(message.sid)

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
