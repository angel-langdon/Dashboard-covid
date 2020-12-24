#!/usr/bin/env python
# coding: utf-8

# In[7]:


import requests
from datetime import datetime, timedelta
import pandas as pd
import json
import os
from difflib import SequenceMatcher
import time


DATA_FOLDER = "./data"
base_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/"
date_format ='%m-%d-%Y' #01-22-2020.csv
df_date_format = '%Y-%m-%d'
communites_list = ['Castilla-Leon',
 'Cataluña',
 'Ceuta',
 'Murcia',
 'La Rioja',
 'Baleares',
 'Canarias',
 'Cantabria',
 'Andalucia',
 'Asturias',
 'Valencia',
 'Melilla',
 'Navarra',
 'Galicia',
 'Aragon',
 'Madrid',
 'Extremadura',
 'Castilla-La Mancha',
 'Pais Vasco']


#communites_geojson = read_communites_geojson()

correspondence_dict = {'Andalusia': 'Andalucia',
 'Aragon': 'Aragon',
 'Asturias': 'Asturias',
 'Baleares': 'Baleares',
 'C. Valenciana': 'Valencia',
 'Canarias': 'Canarias',
 'Cantabria': 'Cantabria',
 'Castilla - La Mancha': 'Castilla-La Mancha',
 'Castilla y Leon': 'Castilla-Leon',
 'Catalonia': 'Cataluña',
 'Ceuta': 'Ceuta',
 'Extremadura': 'Extremadura',
 'Galicia': 'Galicia',
 'La Rioja': 'La Rioja',
 'Madrid': 'Madrid',
 'Melilla': 'Melilla',
 'Murcia': 'Murcia',
 'Navarra': 'Navarra',
 'Pais Vasco': 'Pais Vasco'}

#communities_geojson = read_communites_geojson("spain-communites-v2")

def correspondence_string(string, list_to_match):
    current_ratio = 0
    return_string = None
    for string_from_list in list_to_match:
        ratio = SequenceMatcher(None, string, string_from_list).ratio()
        if ratio > current_ratio:
            current_ratio = ratio
            return_string = string_from_list
    return return_string

def get_correspondence_dict(covid_communities_name, string_list = communites_list):
    dic_correspondence = {}
    for original_string in covid_communities_name:
        dic_correspondence[original_string] = correspondence_string(original_string, string_list)
    return dic_correspondence

#get_correspondence_dict(dfs[0]["Province_State"])


def format_day(day_str):
    day = datetime.strptime(day_str, "%m-%d-%Y")
    return datetime.strftime(day, "%Y-%m-%d")

def read_communites_geojson(name = "spain-communities" ):
    with open(f"./data/geojson/{name}.geojson") as f:
        geojson = json.load(f)
        communites = []
        for region in geojson['features']:
            nameunit = region["properties"]["nameunit"]
            if "/" in nameunit:
                region["properties"]["nameunit"] = nameunit.split("/")[0]
            if 'Ciudad Autónoma de Ceuta' in nameunit:
                region["properties"]["nameunit"] = "Ceuta"
            elif 'Ciudad Autónoma de Melilla' in nameunit:
                region["properties"]["nameunit"] = "Melilla"
            elif 'Comunidad Foral de Navarra' in nameunit:
                region["properties"]["nameunit"] = "Navarra"
            communites.append(region["properties"]["nameunit"])
    return geojson, communites

def get_communites(geojson):
    regions = []
    for region in geojson['features']:
        if region["properties"]["name"] == "Valencia":
            region["properties"]["name"] = "C. Valenciana"
        regions.append(region["properties"]["name"])
    return regions
        

def generate_days(start_date):
    end_date = datetime.now()
    step = timedelta(days=1)
    result = []
    while start_date < end_date:
        result.append(start_date.strftime(date_format))
        start_date += step
    return result




#download_all_datasets()
        
def add_to_list(l, lat_sum, lon_sum):
    # For moving Canary Islands near Spain.
    # l is the list of list of lists .... of coordinates
    if isinstance(l, list) and isinstance(l[0], float) and isinstance(l[1], float):
        return l[0] + lat_sum, l[1] + lon_sum 
    return [add_to_list(sub, lat_sum, lon_sum) for sub in l]

def reduce_precission(l, ndigits):
    if not isinstance(l, list):
        return round(l, ndigits)
    return [reduce_precission(sub, ndigits) for sub in l]


def read_original_to_displaced_canaries():
    lat_sum = 6.65456
    lon_sum = 5.65412
    geojson,b = read_communites_geojson_v1('spain-communities')
    for region in geojson['features']:
        name = region["properties"]["name"]
        if name == "Canarias":
            region["geometry"]["coordinates"] = add_to_list(region["geometry"]["coordinates"],
                                                           lat_sum,
                                                           lon_sum)
    with open(f"./data/geojson/spain-communites-displaced-canary.geojson", "w") as f:
        json.dump(geojson, f)


def read_communites_geojson_v1(name = "spain-communities" ):
    with open(f"./data/geojson/{name}.geojson") as f:
        geojson = json.load(f)
        communites = []
    for region in geojson['features']:
        name = region["properties"]["name"]
        communites.append(name)
            
    return geojson, communites
#communities_geojson,b = read_communites_geojson_v1()


        
def read_population_dataset(name = 'spain-communities-2019.csv'):
    
    def clean_name_pop(name):
        if " " in name:
            name = " ".join(name.split(" ")[1:])
        if "," in name:
            split = name.split(",")
            name = " ".join(split[1:] + [split[0]])
        return name

    def clean_pop_pop(pop):
        if "." in pop:
            return int(pop.replace(".",""))
    population = pd.read_csv(f"./data/population/{name}", sep=";")
    population = population[population["Periodo"] == 2019]
    population = population[population["Sexo"] == "Total"] 
    population.drop(columns=['Periodo', 'Sexo'], inplace=True)
    population['Comunidades y Ciudades Autónomas'] = [clean_name_pop(name) for name in population['Comunidades y Ciudades Autónomas'] ]
    population["Total"] = [clean_pop_pop(pop) for pop in population["Total"]]
    population.loc[population['Comunidades y Ciudades Autónomas'] == "Comunitat Valenciana", 'Comunidades y Ciudades Autónomas'] = 'Valencia'
    population.loc[population['Comunidades y Ciudades Autónomas'] == "Comunidad Foral de Navarra", 'Comunidades y Ciudades Autónomas'] = 'Navarra'
    correspondence_dict_population = get_correspondence_dict(df_diario_acumulado["Comunidad Autónoma"].unique(),population['Comunidades y Ciudades Autónomas'])
    population.rename(columns = {'Comunidades y Ciudades Autónomas': 'Comunidad'}, inplace = True)
    return population, correspondence_dict_population

def get_pop(com):
    com = correspondence_dict_population[com]
    return int(pop_df.loc[pop_df["Comunidad"]==com, 'Total'])

def tasa_mortalidad_y_letalidad(df):
    df["% de letalidad"] = df['Muertes'] * 100 / df['Confirmados'] 
    df["% Población contagiada acumulado"] = df['Confirmados'] * 100 / df["Población"]
    
def obtener_df_semanal(df):
    df["Datetime"] = pd.to_datetime(df['Día'], format=df_date_format)
    df["dia_sem"] = [day.weekday() for day in df['Datetime']]
    df_semanal = df[df["dia_sem"] == 6].copy()
    df.drop(columns= ["dia_sem", 'Datetime'], inplace = True)
    df_semanal.drop(columns = ["dia_sem", 'Datetime'], inplace = True)
    return df_semanal

def save_df(name, df):
    df.to_csv(os.path.join(DATA_FOLDER, "final_data", name),
                encoding='UTF-8',
              sep=";", index= False)
    
def obtener_df_semanal_desacumulado(df):
    dfs_desacumulados = []
    for com in df["Comunidad Autónoma"].unique():
        df_com =  df[df['Comunidad Autónoma']==com].copy()
        for column in ["Confirmados", "Muertes"]:
            df_com.sort_values(by="Día", inplace = True)
            df_com[column] = df_com[column].diff()
        df_com.dropna(inplace = True)
        dfs_desacumulados.append(df_com)
        
    dfs_desacumulado = pd.concat(dfs_desacumulados)
    dfs_desacumulado.drop(['Población',r'% de letalidad',
                    r'% Población contagiada acumulado'],
                         inplace = True,
                         axis = 1)
    dfs_desacumulado.sort_values(by = "Día", inplace = True)
    return dfs_desacumulado


def download_all_datasets():
    start_date = datetime(month = 5, day = 14, year=2020)    
    days = generate_days(start_date)
    descargados = os.listdir(os.path.join(DATA_FOLDER,
                                         "covid_data"))
    for i, day in enumerate(days):
        filename = f"{day}.csv"
        if filename not in descargados:
            try:
                df = pd.read_csv(base_url + filename)
                #df = df.loc[df['Country_Region'] == "Spain"]
                df.to_csv(f"{DATA_FOLDER}/covid_data/{filename}", index = False)
            except:
                print(f"No se ha encontrado el día {day}")

download_all_datasets()
    
dfs = []

for file in sorted(os.listdir(os.path.join(DATA_FOLDER, "covid_data"))):
    if ".csv" in file:
        day = file[:-4]
        df = pd.read_csv(f"{DATA_FOLDER}/covid_data/{file}")
        df = df.loc[(df['Country_Region'] == "Spain") & (df['Province_State'] != "Unknown")]
        df["Province_State"] = [correspondence_dict[province] for province in df["Province_State"]]
        df = df[['Province_State','Country_Region',
                'Last_Update','Confirmed', 
                'Deaths', 'Recovered',
                'Active']]
        df["Day"] = [format_day(day) for i in range(len(df))]
        df.drop(columns = ["Active", 'Recovered', 'Last_Update'], inplace = True)
            
        # df.to_csv("data.csv", index = False)
        dfs.append(df)

df_diario_acumulado = pd.concat(dfs)
df_diario_acumulado.drop(columns=["Country_Region"], inplace = True)
df_diario_acumulado.rename(columns={"Province_State": "Comunidad Autónoma",
                   "Confirmed": "Confirmados",
                  "Deaths": "Muertes",
                   "Day":"Día"}, inplace = True)
pop_df, correspondence_dict_population = read_population_dataset()
df_diario_acumulado['Población'] = df_diario_acumulado["Comunidad Autónoma"].apply(lambda x: get_pop(x))
del pop_df, correspondence_dict_population

tasa_mortalidad_y_letalidad(df_diario_acumulado)
df_semanal_acumulado = obtener_df_semanal(df_diario_acumulado)
df_semanal_desacumulado = obtener_df_semanal_desacumulado(df_semanal_acumulado)

save_df('diario_acumulado.csv', df_diario_acumulado)
save_df('semanal_acumulado.csv', df_semanal_acumulado)
save_df('semanal_desacumulado.csv',df_semanal_desacumulado)


# In[3]:





# In[ ]:




