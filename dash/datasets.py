from utils import read_data
from utils import read_geojson
from server import app
from dash.dependencies import Output, Input


@app.callback(Output('diario-acumulado', 'data'),
              Input('diario-acumulado', 'modified_timestamp'))
def diario_acumulado(ts): return read_data('diario_acumulado.csv').to_json()


# semanal_acumulado = read_data('semanal_acumulado.csv')
# semanal_desacumulado = read_data('semanal_desacumulado.csv')
def diario_acumulado_ultimo(): return read_data('diario_acumulado.csv')[-20:]  # ultimas 20 comunidades


def diario_acumulado_ultimo_sin_total():
    df = read_data('diario_acumulado.csv')[-20:]
    return df[df["Comunidad Autónoma"] != 'Total']  # Eliminado las observaciones que tengan total


geojson_comunidades = read_geojson()
