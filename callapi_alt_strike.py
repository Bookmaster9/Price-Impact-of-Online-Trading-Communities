import pandas as pd
from helper_getquotes import get_quotes
from helper_timefunctions import *
from helper_getstrikes import get_strikes

# Load the data
df = pd.read_excel('allevents.xlsx',index_col=0)
print(df.shape[0], "rows of data have been loaded")
does_not_exist = []
error_codes, error_messages = [], []
for index, row in df.iterrows():
    if index[0] == "O" and int(index[1:]) <= 1745:
        continue
    # Preprocess the rows
    start_time, end_time = time_to_milliseconds_range(surrounding_times(row["Time"]))
    exp_date = raw_to_date(row["Expiration Month"], row["Expiration Day"], row["Expiration Year"])
    right = "C" if row["Option Type"] == "Call" else "P"
    date = int(row["Date"].strftime('%Y%m%d'))
    strike = int(row["Strike"]*1000)
    print("Data preprocessed")

    # Get the strikes
    try:
        strikes = get_strikes(row["Ticker"], exp_date)
        cur_ind = strikes.index(str(strike))
    except:
        does_not_exist.append(row)
        error_codes.append("N/A")
        error_messages.append("Strike does not exist")
        continue
    try:
        neighboring_strikes = {"-2":strikes[cur_ind-2], "-1":strikes[cur_ind-1], "+1":strikes[cur_ind+1], "+2":strikes[cur_ind+2]}
    except:
        does_not_exist.append(row)
        error_codes.append("N/A")
        error_messages.append("Strike does not exist")
        continue

    for strike_offset in neighboring_strikes:

        strike = neighboring_strikes[strike_offset]

        # Get the exact quote from 1 minute before to 5 minutes after each second
        data = get_quotes(row["Ticker"], exp_date, strike, right, date, date, start_time, end_time)

        # If there is an error in obtaining
        if isinstance(data, tuple):
            does_not_exist.append(row)
            error_codes.append(data[0])
            error_messages.append(data[1])
            continue
        print("Data received")

        # Save the data
        data.to_csv(f"databeforeafter/{index}_{strike_offset}.csv", index = False)
        print("saved ", index, strike_offset)

# Output the rows that do not exist
dne = pd.DataFrame(does_not_exist)
dne["Error Code"] = error_codes
dne["Error Message"] = error_messages
dne.to_csv("alt_strike_does_not_exist.csv", index = False)
