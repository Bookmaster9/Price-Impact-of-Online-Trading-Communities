import pandas as pd
# Read in entered_long_all.txt
with open('entered_long_all.txt', 'r') as file:  # Open the file in read mode
    content = file.read()           # Read the entire file

# split content by XcaptureAPP
content = content.split('XcaptureAPP')

index = 0

dates = []
times = []
tickers = []
expr_months = []
expr_days = []
expr_years = []
strikes = []
option_types = []
prices = []
risks = []
directions = []
weirdones = ""
weirdones2 = ""

for message in content:
    if message.count("entered long") == 1 and message.count("web platform.  Closed") == 0 and message.count("web platform.  Exited") == 0 and message.count("Average accepted") == 0 and message.count("Partial exit") == 0 and message.count("Exited") == 0:
        timestamp = message.split("—")[1].split("@everyone")[0].strip()
        if message.count("Today") < 1 and message.count("Yesterday") < 1:
            date = timestamp.split(", ")[0]
            time = timestamp.split(", ")[1]
        elif message.count("Today ") == 1:
            date = "Today"
            time = timestamp.split(" at ")[1]
        elif message.count("Yesterday ") == 1:
            date = "Yesterday"
            time = timestamp.split(" at ")[1]
        if message.count("from the web platform") == 1:
            print(message)
            split_trade_info = message.split("platform.  Long")[1].split("|")[0].strip().split(" ")
        else:
            split_trade_info = message.split("entered long")[1].strip().split("|")[0].strip().split(" ")
        try:
            ticker = split_trade_info[0]
            if ticker == "Long":
                split_trade_info = split_trade_info[1:]
                ticker = split_trade_info[0].strip()
            expr_month = split_trade_info[1].strip()
            expr_day = split_trade_info[2].strip()
            expr_year = split_trade_info[3].strip()
            strike = split_trade_info[4].strip()
            option_type = split_trade_info[5].strip()
            price = split_trade_info[7].strip()
            if "$" in price:
                price = price.split("$")[1]
            if "\n" in price:
                price = price.split("\n")[0].strip()
            risk = message.split("Risk ")[1].split(" ")[0].strip()
            dates.append(date)
            times.append(time)
            tickers.append(ticker)
            expr_months.append(expr_month)
            expr_days.append(expr_day)
            expr_years.append(expr_year)
            strikes.append(strike)
            option_types.append(option_type)
            prices.append(price)
            risks.append(risk)
            directions.append("Long")
        except:
            weirdones += message + "\n\n\n"
    else:
        weirdones2 += message + "\n\n\n"
# Return a csv of the data
df = pd.DataFrame(list(zip(dates, times, tickers, expr_months, expr_days, expr_years, strikes, option_types, prices, risks, directions)), columns =['Date', 'Time', 'Ticker', 'Expiration Month', 'Expiration Day', 'Expiration Year', 'Strike', 'Option Type', 'Price', 'Risk', 'Direction'])
df.to_csv('entered_long_all.csv', index=False)
with open('weirdones.txt', 'w') as file:
    file.write(weirdones)
with open('weirdones2.txt', 'w') as file:
    file.write(weirdones2)
        
        
    
