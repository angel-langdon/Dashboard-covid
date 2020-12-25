import pandas as pd
import json


def read_data(name):
    # return pd.read_csv(os.path.join(DATA_FOLDER, name), sep=";")
    # base_url = "https://entredatos.es/dashboard-covid/final_data/"
    base_url = "../data/final_data/"
    complete_url = f"{base_url}{name}"
    return pd.read_csv(complete_url, sep=";")


def read_geojson(name='spain-communities-displaced-original-compressed.geojson'):
    base_url = "../data/geojson/"
    complete_url = f"{base_url}{name}"
    with open(complete_url) as f:
        geojson = json.load(f)
    return geojson

