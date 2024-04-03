import requests
import os
import json
import pandas as pd

pd.set_options('display.max_columns', 500)

api_key = os.getenv("NREL_API_KEY")
# Perform a GET request using Requests

req_url = "https://developer.nrel.gov/"
endpoint_url = "api/alt-fuel-stations/v1.json?api_key={}&status=E&fuel_type=all".format(api_key)
req_url = req_url + endpoint_url

response = requests.get(req_url)
response = json.loads(response.content)

df = pd.DataFrame(list(response['fuel_stations']))

print(df.head())