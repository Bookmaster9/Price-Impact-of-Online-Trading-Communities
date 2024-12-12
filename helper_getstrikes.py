import httpx  # install via pip install httpx
import csv

BASE_URL = "http://127.0.0.1:25510/v2"  # all endpoints use this URL base

def get_strikes(root, exp):    
    params = {
        'root': root,
        'exp': exp,
        'use_csv': True
    }
    url = BASE_URL + '/list/strikes'

    while url is not None:
        response = httpx.get(url, params=params)  # make the request
        response.raise_for_status()  # make sure the request worked

        # read the entire response, and parse it as CSV
        csv_reader = csv.reader(response.text.split("\n"))

        all_strikes = []
        for index, strike in enumerate(csv_reader):
            if index == 0:
                continue
            if strike:
                all_strikes.append(strike[0])

        # check the Next-Page header to see if we have more data
        if 'Next-Page' in response.headers and response.headers['Next-Page'] != "null":
            url = response.headers['Next-Page']
        else:
            url = None
    return all_strikes
