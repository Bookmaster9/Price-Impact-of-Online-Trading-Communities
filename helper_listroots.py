import httpx  # install via pip install httpx
import csv

BASE_URL = "http://127.0.0.1:25510/v2"  # all endpoints use this URL base

# set params
params = {
	'use_csv': 'true',
}

#
# This is the non-streaming version, and the entire response
# will be held in memory.
#
url = BASE_URL + '/list/roots/stock'

while url is not None:
    response = httpx.get(url, params=params)  # make the request
    response.raise_for_status()  # make sure the request worked

    # read the entire response, and parse it as CSV
    csv_reader = csv.reader(response.text.split("\n"))

    for row in csv_reader:
        print(row)  # do something with the data

    # check the Next-Page header to see if we have more data
    if 'Next-Page' in response.headers and response.headers['Next-Page'] != "null":
        url = resp.headers['Next-Page']
    else:
        url = None

