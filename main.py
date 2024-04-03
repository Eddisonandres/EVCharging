import requests
import os

api_key = os.getenv("NREL_API_KEY")
# Perform a GET request using Requests

req_url = "developer.nrel.gov/"
endpoint_url = "api/alt-fuel-stations/v1.json?{}".format(api_key)
req_url = req_url + endpoint_url

response = requests.get(req_url)

print(response)
print("=" * 50)
print(response.content)