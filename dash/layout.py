from components.title import title
from components.confirmados_muertes_letalidad_barras_verticales import confirmados_muertes_letalidad_barras_verticales
from components.mapa_acumulado import mapa_acumulado
from components.grafico_lineas import grafico_lineas
from components.footer import footer
from components.divider import divider
import constants as cons
from utils import read_data, read_geojson
import dash_html_components as html

DATA_FOLDER = "./data/final_data"
diario_acumulado = read_data('diario_acumulado.csv')
semanal_acumulado = read_data('semanal_acumulado.csv')
semanal_desacumulado = read_data('semanal_desacumulado.csv')
diario_acumulado_ultimo = diario_acumulado[-20:].copy()
diario_acumulado_ultimo_sin_total = diario_acumulado_ultimo[diario_acumulado_ultimo["Comunidad Autónoma"]!='Total'].copy()
geojson_comunidades = read_geojson()


def layout(app):
    return html.Div(children=[
        title(),
        divider,
        mapa_acumulado(diario_acumulado_ultimo_sin_total, geojson_comunidades, cons, diario_acumulado_ultimo),
        html.Br(),
        divider,
        confirmados_muertes_letalidad_barras_verticales(diario_acumulado_ultimo_sin_total, cons),
        divider,
        grafico_lineas(diario_acumulado, cons, app),

        html.Br(),

        footer(list(diario_acumulado_ultimo_sin_total['Día'])[0])

    ])
