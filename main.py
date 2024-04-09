import requests
import os
import json
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()


pd.set_option('display.max_columns', 500)

api_key = os.getenv("NREL_API_KEY")

def get_ev_chargers(_api_key, ret_amount):
    req_url = "https://developer.nrel.gov/api/alt-fuel-stations/v1.json?api_key={}&status=E&fuel_type=ELEC&ev_network=Tesla&limit={}".format(_api_key, ret_amount)
    response = requests.get(req_url)
    response = json.loads(response.content)
    df = pd.DataFrame(response['fuel_stations'])
    df = df[['station_name',"date_last_confirmed", "latitude", "longitude"]]
    return df

ev_chargers = get_ev_chargers(api_key, 1)

user_name = "eddison"
ps = os.getenv("local_pass")
engine = create_engine("postgresql+psycopg2://{}:{}@localhost:5432/DB_Development".format(user_name,ps))


ev_chargers.to_sql("ev_charger",con=engine, if_exists="replace")