import pandas as pd
import json
from numpy import floating, integer


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


def beautify_number(number):
    if isinstance(number, (float, floating)):
        if number.is_integer():
            return beautify_number(int(number))
        return round(number, 4)
    elif isinstance(number, (int, integer)):
        number = str(number)[::-1]
        return ' '.join(number[i:i + 3] for i in range(0, len(number), 3))[::-1]
