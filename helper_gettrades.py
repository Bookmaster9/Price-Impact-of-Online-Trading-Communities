import httpx  # install via pip install httpx
import csv
import pandas as pd

BASE_URL = "http://127.0.0.1:25510/v2"  # all endpoints use this URL base

def get_trades(root, exp, strike, right, start_date, end_date,start_time, end_time, use_csv = True, ivl = 1000):
    params = {
        'root': root,
        'exp': exp,
        'strike': strike,
        'right': right,
        'start_date': start_date,
        'end_date': end_date,
        'use_csv': use_csv,
        "start_time": start_time,
        "end_time": end_time
    }

    url = BASE_URL + '/hist/option/trade'

    all_data = []

    while url is not None:
        try:
            response = httpx.get(url, params=params)  # make the request
            response.raise_for_status()  # make sure the request worked
        except httpx.HTTPStatusError as exc:
            status_code = exc.response.status_code
            error_message = exc.response.text  # Extract response text for debugging
            print(f"Error occurred: HTTP {status_code}")
            print(f"Error details: {error_message}")
            return status_code, error_message

        # read the entire response, and parse it as CSV
        csv_reader = csv.reader(response.text.split("\n"))
        
        for index, row in enumerate(csv_reader):
            if index == 0:
                header = row
                continue
            all_data.append(row)

        # check the Next-Page header to see if we have more data
        if 'Next-Page' in response.headers and response.headers['Next-Page'] != "null":
            url = response.headers['Next-Page']
        else:
            url = None
    return pd.DataFrame(all_data, columns=header)