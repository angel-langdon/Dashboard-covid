from utils import read_data
from utils import read_geojson


def diario_acumulado(): return read_data('diario_acumulado.csv')


# semanal_acumulado = read_data('semanal_acumulado.csv')
# semanal_desacumulado = read_data('semanal_desacumulado.csv')
def diario_acumulado_ultimo(): return diario_acumulado()[-20:]


def diario_acumulado_ultimo_sin_total():
    df = diario_acumulado_ultimo()
    return df[df["Comunidad Autónoma"] != 'Total']


geojson_comunidades = read_geojson()
