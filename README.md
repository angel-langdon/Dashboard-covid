# Dashboard-covid

## Pasos para poder ejecutarlo en local:

### 1º Abrir una terminal y cambiar el directorio hasta estar en la carpeta
> cd /Users/tusuario/la_carpeta_donde_guardes_el_dashboard/Dashboard-covid

### 2º Instalar los paquetes necesarios para poder ejecutar los scripts
Se pueden instalar manualmente con este comando: 
> pip install -r requirements.txt

O bien manualmente instalando los paquetes que están descritos en requirements.txt

### 2º Ejecutar los siguientes comandos:
> cd dash

> python index.py

### 3º Dirigirse a esta dirección 

 http://127.0.0.1:8050/dashboard/covid-19-spain/
 
 
 ## ¿Qué hace cada archivo?
 
 ./
    cronjob.txt # la periodización de la descarga de los datos para que se actualicen automáticamente
    LICENSE
    requirements.txt # los paquetes necesarios
    README.md
    download_data.py # el script que se ejecuta cada cierto tiempo para que los datos estén actualizados
    dash/
        server.py
        index.py
        layout.py
        constants.py
        datasets.py
        utils.py
        components/     # Aquí están los componentes que forman los dashboard, cada componente el html y los gráficos que forman cada una de las partes 
            information.py
            grafico_lineas.py
            mapa_acumulado.py
            divider.py
            footer.py
            kpi.py
            confirmados_muertes_letalidad_barras_verticales.py
            title.py
    data/
        geojson/
            spain-communities.geojson
            spain-communities-displaced-original-compressed-small-cities.geojson
            spain-communities-displaced-original-compressed.geojson
            spain-communites-displaced-canary.geojson
        population/
            spain-communities-2020.csv
        covid_data/
            # Aquí están todos los CSV
            05-18-2020.csv
            11-10-2020.csv
            11-11-2020.csv
            07-16-2020.csv
            07-17-2020.csv
            01-06-2021.csv
        final_data/
            semanal_acumulado.csv
            diario_acumulado.csv
            semanal_desacumulado.csv
 
 
 
